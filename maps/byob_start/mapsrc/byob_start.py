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


messages = {
    'msg_id': """
žWe wish all the best to
everyone impacted by the mass layoffs
at MicrosoftžŸ

We all love you very much
""",
    'msg_roj': """
Here Lyeth the body of RecycledOJs map.
Maye its beautiful arches and brickworke
rest in peace.
    """,
    'msg_squid': """
Here Lyeth the body of Squid V's map.
Considere getting thyself a Tetanus shot
after visiting mine Hallowed ground.
""",
    'msg_ehot': """
Here lyeth the body of EHOTs map,
even a crumbling castle can be
fertile ground for moss to take root
""",
    'msg_4lt': """
Here lyeth the body of 4lts map,
i was once a house,
flora groweth through me now.
now i am a greenhouse!
""",
    'msg_shinko': """
Here lyeth the body of Shinkos' map,
In the great void,\
noman shalt heareth thy shrill cry...
""",
    'msg_nova': """
Here lyeth the map of Novafrost,
Someday this door will open, til then --
may these funny lil' dudes keep thee company.
""",
    'msg_moko': """
Here lyeth the map of Moko...
Patterns sharp, and colors bold,
may this shelter shield thee from the cold...
""",
    'msg_auhsan': """
Here lyeth the map of Auhsan,
beautiful bricks of many a hue,
may my glistening pool shineth light upon you!
""",
}


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
                if message.startswith('$msg_'):
                    ent.kv['message'] = messages[message].replace('\n', r'\n')
                elif message.startswith('$'):
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
