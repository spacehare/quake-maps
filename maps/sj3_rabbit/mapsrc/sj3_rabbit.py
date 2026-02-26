# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


import copy

from rabbitquake.app.parse import Brush, Entity

replace_proto = {
    'a': 'b',
}


def clip(ent: Entity) -> list[Brush]:
    output_brushes: list[Brush] = []
    for brush in ent.brushes:
        clone = copy.deepcopy(brush)
        for plane in clone.planes:
            plane.texture_name = 'clip'
        output_brushes.append(clone)
    return output_brushes


def replace_texture(ent: Entity, a: str, b: str):
    for brush in ent.brushes:
        for face in brush.planes:
            if face.texture_name == a:
                face.texture_name = b


def main(context: dict) -> list[Entity]:
    VAR_PREFIX: str = context['var_prefix']
    EVAL_PREFIX = VAR_PREFIX + 'eval'
    input_entities: list[Entity] = list[Entity](context['entities'])
    output_entities: list[Entity] = []

    assert input_entities[0].classname == 'worldspawn'
    worldspawn: Entity = input_entities[0]

    for ent in input_entities:
        # delete
        if ent.kv.get(VAR_PREFIX + 'delete') == '1':
            continue

        # eval
        for key in ent.kv:
            if ent.kv[key].startswith(EVAL_PREFIX):
                ent.kv[key] = eval(ent.kv[key].removeprefix(EVAL_PREFIX))

        # clip
        if ent.kv.get(VAR_PREFIX + 'clip') == '1':
            worldspawn.brushes += clip(ent)

        for key in ent.kv:
            # 40 char limit warning
            if key == 'message':
                split = ent.kv[key].split('\\n')
                for line in split:
                    if len(line) > 40:
                        print('LINE GREATER THAN 40!\n%s' % line)

        # replace proto textures
        for key in replace_proto:
            replace_texture(ent, key, replace_proto[key])

        match ent.classname:
            case 'func_door':
                ent.kv.setdefault('speed', '128')
                ent.kv.setdefault('sounds', '2')
            case 'func_button':
                ent.kv.setdefault('speed', '64')
                ent.kv.setdefault('sounds', '2')
            case 'trigger_textstory':
                del ent.kv['mangle']

        output_entities.append(ent)

    return output_entities
