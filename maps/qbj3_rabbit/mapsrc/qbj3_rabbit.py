# this Python file contains code to pre-process the MAP file

# https://github.com/spacehare/rabbit_quake


import copy
from enum import Enum

from rabbitquake.app.parse import Brush, Entity


class EntitySkillflags(Enum):
    NOT_ON_EASY = 256  # '0b00100000000'
    NOT_ON_NORMAL = 512  # '0b01000000000'
    NOT_ON_HARD = 1024  # '0b10000000000'


SYMBOL_COUNT = '#'


def autocount(trigger_counter: Entity, entities: list[Entity]) -> list[Entity] | None:
    if not ((count_value := trigger_counter.kv.get('count')) and count_value.startswith(SYMBOL_COUNT)):
        return

    totals: list[int] = [0] * 3

    # check who is targeting the trigger_counter
    for entity in [e for e in entities if e is not trigger_counter]:
        for key in entity.kv:
            if key.startswith('target') and entity.kv[key] == trigger_counter.kv['targetname']:
                # skill flags
                if possible_flags := entity.kv.get('spawnflags'):
                    spawnflags: int = int(possible_flags)

                    is_easy = not (EntitySkillflags.NOT_ON_EASY.value & spawnflags)
                    is_normal = not (EntitySkillflags.NOT_ON_NORMAL.value & spawnflags)
                    is_hard = not (EntitySkillflags.NOT_ON_HARD.value & spawnflags)

                    skill_bools = (is_easy, is_normal, is_hard)

                    for idx, skill_bool in enumerate(skill_bools):
                        if skill_bool:
                            totals[idx] += 1

                else:
                    totals = [i + 1 for i in totals]

    clones = []
    for idx, skill_flag in enumerate(EntitySkillflags):
        if totals[idx] == 0:
            continue

        # set count
        clone: Entity = copy.deepcopy(trigger_counter)
        clone.kv['count'] = str(totals[idx])

        # unset "NOT ON <SKILL>" for the one we want
        clone_spawnflags = int(clone.kv.get('spawnflags', 0)) & ~skill_flag.value
        # set "NOT ON <SKILL>" for the ones we don't
        for skill in [flag for flag in EntitySkillflags if flag is not skill_flag]:
            clone_spawnflags |= skill.value

        clone.kv['spawnflags'] = str(clone_spawnflags)

        clones.append(clone)

    return clones


def clip(ent: Entity) -> list[Brush]:
    output_brushes: list[Brush] = []
    for brush in ent.brushes:
        clone = copy.deepcopy(brush)
        for plane in clone.planes:
            plane.texture_name = 'clip'
        output_brushes.append(clone)
    return output_brushes


def main(context: dict) -> list[Entity]:
    print('🐇 running qbj3_rabbit.py')

    var_prefix: str = context['var_prefix']
    input_entities: list[Entity] = context['entities']
    output_entities: list[Entity] = []

    print('prefix: %s' % var_prefix)

    assert input_entities[0].classname == 'worldspawn'
    worldspawn: Entity = input_entities[0]

    for ent in input_entities:
        if ent.kv.get(var_prefix + 'delete') == '1':
            continue
        elif result := autocount(ent, input_entities):
            output_entities += result
            continue

        for key in ent.kv:
            if ent.kv[key].startswith('eval'):
                ent.kv[key] = eval(ent.kv[key].removeprefix('eval'))

        if ent.kv.get(var_prefix + 'clip') == '1':
            worldspawn.brushes += clip(ent)

        # door
        if ent.classname == 'func_door':
            ent.kv.setdefault('_minlight', '50')
            ent.kv.setdefault('sounds', '3')
            ent.kv.setdefault('_dirt', '-1')

        # purge angles
        if (
            ent.classname.startswith('trigger')
            and not ent.kv.get(var_prefix + 'use_angle') == '1'
            and ent.kv.get('angle')
            and not ent.classname.endswith('monsterjump')
        ):
            print('clearing angle on %s' % ent.classname)
            del ent.kv['angle']

        # texture swapping
        # redundant bc of: https://pwitvoet.github.io/mess/entity-properties.html#_mess_replace_texture
        if tex := ent.kv.get(var_prefix + 'replace_texture_from'):
            for brush in ent.brushes:
                for face in brush.planes:
                    if face.texture_name == tex:
                        face.texture_name = ent.kv[var_prefix + 'replace_texture_with']

        output_entities.append(ent)

    return output_entities
