# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


from rabbitquake.app.parse import Entity
from rabbitquake.ppdefs import clip

replace_proto = {
    '*': 'sky_void',
}


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
                if face.texture_name != '*tele01':
                    face.uv.u.scale = 0.25
                    face.uv.v.scale = 0.25
                    face.uv.u.offset = 0.0
                    face.uv.v.offset = 0.0

        if ent.classname.startswith('item'):
            ent.kv['angle'] = '0'

        match ent.classname:
            case 'func_door':
                ent.kv.setdefault('speed', '128')
                ent.kv.setdefault('sounds', '1')
            case 'func_detail_illusionary':
                if ent.kv.get(VAR_PREFIX + 'clip') == '1':
                    worldspawn.brushes += clip.clip(ent)
            case 'monster_enforcer':
                ent.kv['ammo_nails'] = '-5'
