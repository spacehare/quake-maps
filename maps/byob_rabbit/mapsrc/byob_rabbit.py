# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


from rabbitquake.app.parse import Entity
from rabbitquake.ppdefs import autocount

replace_proto = {
    'bun_proto1': 'bun_flat',
    'bun_proto2': 'bun_flat',
    'sky': 'sky_compat',
}

waterlist = ['*bun_portal', '*bun_slime', '*bun_water']


def replace_texture(ent: Entity, a: str, b: str) -> None:
    for brush in ent.brushes:
        for face in brush.planes:
            if face.texture_name == a:
                face.texture_name = b


def main(input: list[Entity], context: dict) -> None:
    VAR_PREFIX: str = context['var_prefix']
    EVAL_PREFIX = VAR_PREFIX + 'eval'

    assert input[0].classname == 'worldspawn'

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
                ent.kv.setdefault('sounds', '1')
            case 'trigger_counter':
                if result := autocount.autocount(ent, input):
                    input += result
                    assert result[0] in input
                    input.remove(ent)
                    continue
