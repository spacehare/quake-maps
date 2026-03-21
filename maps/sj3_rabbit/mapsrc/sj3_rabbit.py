# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


from rabbitquake.app.parse import Entity
from rabbitquake.ppdefs import autocount, clip

replace_proto = {
    '*': 'skip',
    'dot_grey_c': 'sj3_grayfloor',
    'floor_grey_c': 'sj3_grayfloor',
    'wall_grey_a': 'sj3_grayfloor',
    'wall_grey_b': 'sj3_grayfloor',
    'wall_orange_a': 'sj3_orange',
    'wall_orange_b': 'sj3_orange',
}

waterlist = ['*slime_sj3', '*sj3_water', '*tele_sj3']


def replace_texture(ent: Entity, a: str, b: str) -> None:
    for brush in ent.brushes:
        for face in brush.planes:
            if face.texture_name == a:
                face.texture_name = b


def main(input: list[Entity], context: dict) -> None:
    VAR_PREFIX: str = context['var_prefix']
    EVAL_PREFIX = VAR_PREFIX + 'eval'
    # input = list[Entity](context['entities'])

    assert input[0].classname == 'worldspawn'
    worldspawn: Entity = input[0]

    for ent in input:
        # delete
        if ent.kv.get(VAR_PREFIX + 'delete') == '1':
            input.remove(ent)
            continue

        # eval
        for key in ent.kv:
            if ent.kv[key].startswith(EVAL_PREFIX):
                ent.kv[key] = eval(ent.kv[key].removeprefix(EVAL_PREFIX))

        # replace proto textures
        for key in replace_proto:
            replace_texture(ent, key, replace_proto[key])

        for brush in ent.brushes:
            for face in brush.planes:
                if face.texture_name in waterlist:
                    face.uv.u.scale = 2.0
                    face.uv.v.scale = 2.0
                    face.uv.u.offset = 0.0
                    face.uv.v.offset = 0.0

        match ent.classname:
            case 'func_door':
                ent.kv.setdefault('speed', '128')
                ent.kv.setdefault('sounds', '2')
            case 'func_button':
                ent.kv.setdefault('speed', '64')
                ent.kv.setdefault('sounds', '2')
            case 'trigger_textstory':
                del ent.kv['mangle']
            case 'func_detail_illusionary':
                if ent.kv.get(VAR_PREFIX + 'clip') == '1':
                    worldspawn.brushes += clip.clip(ent)
            case 'trigger_counter':
                if result := autocount.autocount(ent, input):
                    input += result
                    print('template', ent.kv['origin'])
                    print('copy 0', result[0].kv['origin'])
                    assert result[0] in input
                    input.remove(ent)
                    continue
