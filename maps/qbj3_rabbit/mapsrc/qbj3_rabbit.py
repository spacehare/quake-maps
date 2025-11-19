# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

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
        monster_count: int = 1

        # respawning monsters, like in copper
        if entity.classname.startswith('monster'):
            if respawn_count := entity.kv.get('count'):
                monster_count = int(respawn_count)

        # skill flags
        if possible_spawnflags := entity.kv.get('spawnflags'):
            spawnflags: int = int(possible_spawnflags)

            is_easy = not (EntitySkillflags.NOT_ON_EASY.value & spawnflags)
            is_normal = not (EntitySkillflags.NOT_ON_NORMAL.value & spawnflags)
            is_hard = not (EntitySkillflags.NOT_ON_HARD.value & spawnflags)

            monster_skill_bools = (is_easy, is_normal, is_hard)
        else:
            monster_skill_bools = (True, True, True)

        # handle target1, target2, target4, target4, etc
        for key in [k for k in entity.kv if k.startswith('target')]:
            if entity.kv[key] == trigger_counter.kv['targetname']:
                for idx, skill_bool in enumerate(monster_skill_bools):
                    if skill_bool:
                        totals[idx] += monster_count

    # create new trigger_counter copies, per-skill
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
    EVAL_PREFIX = var_prefix + 'eval'
    input_entities: list[Entity] = list[Entity](context['entities'])
    output_entities: list[Entity] = []

    print('prefix: %s' % var_prefix)

    assert input_entities[0].classname == 'worldspawn'
    worldspawn: Entity = input_entities[0]

    for ent in input_entities:
        # delete
        if ent.kv.get(var_prefix + 'delete') == '1':
            continue

        # autocount
        elif result := autocount(ent, input_entities):
            output_entities += result
            continue

        # eval
        for key in ent.kv:
            if ent.kv[key].startswith(EVAL_PREFIX):
                ent.kv[key] = eval(ent.kv[key].removeprefix(EVAL_PREFIX))

        # clip
        if ent.kv.get(var_prefix + 'clip') == '1':
            worldspawn.brushes += clip(ent)

        # ladders
        if ent.kv.get(var_prefix + 'makkon_ladder'):
            keys = ['_mirrorinside', '_phong']
            for key in keys:
                ent.kv[key] = '1'

        # blood
        for brush in ent.brushes:
            for face in brush.planes:
                if face.texture_name == '*gore_blood02':
                    for axis in face.uv:
                        axis.scale = 2.0
                        axis.offset = 0.0

        # door
        if ent.classname == 'func_door':
            ent.kv.setdefault('_minlight', '50')
            ent.kv.setdefault('sounds', '3')
            ent.kv.setdefault('_dirt', '-1')
            ent.kv.setdefault('speed', '128')

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
