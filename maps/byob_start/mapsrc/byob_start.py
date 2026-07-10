# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


import csv
from pathlib import Path

from rabbitquake.app.parse import Entity
from rabbitquake.ppdefs import autocount

replace_proto = {
    # 'bun_proto1': 'bun_flat',
    # 'bun_proto2': 'bun_flat',
    'sky': 'sky_compat',
}

waterlist = ['*bun_portal', '*bun_slime', '*bun_water']


# https://docs.python.org/3/library/csv.html
def read_csv() -> list[dict]:
    SUBMISSIONS = Path(__file__).parent / 'BYOB - submissions.tsv'
    reader = csv.DictReader(SUBMISSIONS.read_text().splitlines(), delimiter='\t')
    obj = [row for row in reader]
    return obj


submission_data: list[dict] = read_csv()


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
            case 'trigger_changelevel':
                ent.kv['target'] = '_ITEMS.SHOTGUN25'
            case 'trigger_multiple':
                message = ent.kv.get('message', '')
                if message.startswith('$'):
                    for item in submission_data:
                        if item['variable'] == message:
                            nick = item['nickname']
                            title = item['message']
                            flavor = item['wons flavor']
                            new_message = rf'[\b{title}\b]\nby \b{nick}\b\n\n{flavor}'
                            ent.kv['message'] = new_message
            case 'func_wall':
                if ent.kv.get(VAR_PREFIX + 'window') == '1':
                    ent.kv['alpha'] = str(1 / 3)
            case 'func_door':
                ent.kv.setdefault('speed', '128')
                ent.kv.setdefault('sounds', '1')
            case 'trigger_counter':
                if result := autocount.autocount(ent, input):
                    input += result
                    assert result[0] in input
                    input.remove(ent)
                    continue
