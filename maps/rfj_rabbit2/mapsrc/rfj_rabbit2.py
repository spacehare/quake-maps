# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# works with this commit version:
# https://github.com/spacehare/rabbit_quake/tree/c44606516e67bee92d3075ca2d9ab0b21482eef5
# ---
# https://github.com/spacehare/rabbit_quake


import copy

from rabbitquake.app.parse import Brush, Entity

RQ_VERSION = 1

replace_proto = {
    'trim_band_red': 'tch_t2_grey1',
    '64_blood_1': 'tch_c1_grey1',
    '16_honey_1': 'sky1',
    'honey_1': 'tch_c1_ylw1',
    'blue_3': 'tch_c1_blu1',
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
    print('running %s' % __file__)

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

        # io decals
        if ent.kv.get(VAR_PREFIX + 'io') == '1':
            ent.kv['_minlight'] = '246'
            ent.kv['_lightignore'] = '1'

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

        # delete keys to get rid of `developer 1` warnings
        trash_list = [key for key in ent.kv if key.startswith(VAR_PREFIX)]
        for key in trash_list:
            del ent.kv[key]

        output_entities.append(ent)

    return output_entities
