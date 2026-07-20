# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


import csv
from copy import deepcopy
from pathlib import Path

from rabbitquake.app.parse import Entity
from rabbitquake.ppdefs import autocount

replace_proto = {
    'sky': 'sky_compat',
    '64_cyan_1': 'hub_grass',
}

replace = [
    'bun_proto1',
    'bun_proto2',
    'hub_check64',
    'hub_check128',
    '128_grey_2',
    '32_grey_1',
    '32_grey_2',
    '64_blood_1',
    '64_blood_2',
    '64_blood_3',
    '64_brown_3',
]

# for re-scaling
water = {
    '*pm_tele': 0.5,
    '*rabbit_tele': 2.0,
    '*razzz_tele': 2.0,
    '*puppluka_tele': 2.0,
    '*chaosed0_tele': 8.0,
    '*cc_tele': 2.0,
}

messages = {
    'msg_id': """
We wish all the best to
everyone impacted by the mass layoffs
at Microsoft

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
In the great void,
noman shalt heareth thy shrill cry...
""",
    'msg_nova': """
Here lyeth the map of Novafrost,
Someday this door will open, til then --
may these funny lil' dudes
keep thee company.
""",
    'msg_moko': """
Here lyeth the map of Moko...
Patterns sharp, and colors bold,
may this shelter shield thee from the cold...
""",
    'msg_auhsan': """
Here lyeth the map of Auhsan,
beautiful bricks of many a hue,
may my glistening pool
shineth light upon you!
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
    EVAL = VAR_PREFIX + 'eval'

    assert input[0].classname == 'worldspawn'
    append_ents: list[Entity] = []

    i = 0
    for ent in input:
        # delete
        if ent.kv.get(VAR_PREFIX + 'delete') == '1':
            input.remove(ent)
            continue

        # eval
        for key in ent.kv:
            if ent.kv[key].startswith(EVAL):
                ent.kv[key] = eval(ent.kv[key].removeprefix(EVAL))

        # replace proto textures
        for key in replace_proto:
            replace_texture(ent, key, replace_proto[key])
        for tex in replace:
            replace_texture(ent, tex, 'hub_noise_a')

        for brush in ent.brushes:
            for face in brush.planes:
                for texname, size in water.items():
                    if face.texture_name == texname:
                        face.uv.u.scale = size
                        face.uv.v.scale = size
                match face.texture_name:
                    case '{hub_flamboyant':
                        face.texture_name = '{hub_flam2'
                        if ent.classname == 'func_detail_illusionary':
                            ent.kv.setdefault('_minlight', '255')
                            ent.kv.setdefault('_minlight_color', '255 239 206')
                    case 'hub_grass':
                        face.uv.u.offset = 0.0
                        face.uv.v.offset = 0.0

        if ent.kv.get(VAR_PREFIX + 'resetuv'):
            for brush in ent.brushes:
                for face in brush.planes:
                    face.uv.u.offset = 0.0
                    face.uv.v.offset = 0.0
                    face.uv.u.scale = 1.0
                    face.uv.v.scale = 1.0

        if ent.kv.get('_surflight_group') == '1':
            ent.kv['_minlight'] = '175'
            ent.kv['_minlight_color'] = '255 239 206'
            ent.kv['_dirt'] = '-1'

        match ent.classname:
            case 'light':
                # for the central pillar ceiling lights
                if ent.kv.get(VAR_PREFIX + 'ceilinglight') == '1':
                    ent.kv['delay'] = '5'
                    ent.kv.setdefault('wait', str(2 / 3))
                    ent.kv.setdefault('light', '100')
                    dc = deepcopy(ent)
                    dc.kv['delay'] = '0'
                    dc.kv['wait'] = '1'
                    dc.kv['light'] = '150'
                    dc.kv['_color'] = '255 239 206'
                    dc.kv['_bounce'] = '-1'
                    append_ents.append(dc)

            case 'trigger_changelevel':
                ent.kv['target'] = '_ITEMS.SHOTGUN25'

            case 'func_button':
                if ent.kv.get(VAR_PREFIX + 'nmbutton') == '1':
                    button_name = f'nm_btn_{i}'
                    ent.kv['targetname'] = button_name
                    ent.kv['killtarget'] = button_name
                    ent.kv['target'] = 'nm.counter'
                    ent.kv['health'] = '1'
                    ent.kv['wait'] = '-1'
                    ent.kv['speed'] = '999'
                    ent.kv['angle'] = '-2'

            case 'trigger_multiple':
                if ent.kv.get('angles'):
                    del ent.kv['angles']
                if ent.kv.get('angle'):
                    del ent.kv['angle']
                message = ent.kv.get('message', '')
                if message.startswith('$msg_'):
                    ent.kv['message'] = messages[message[1:]].replace('\n', r'\n')
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

        i += 1
    input += append_ents
