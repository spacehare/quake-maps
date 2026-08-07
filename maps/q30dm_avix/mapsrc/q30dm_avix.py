# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake


import copy

from rabbitquake.app.parse import Entity

replace_proto = {
    'bun_proto1': 'bun_flat',
    'bun_proto2': 'bun_flat',
    'sky': 'sky_compat',
}


def hex_rgb(string: str):
    # https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    string = string[1:]
    val = [str(int(string[i : i + 2], 16)) for i in (0, 2, 4)]
    return ' '.join(val)


ent_light5 = Entity()
ent_light2 = Entity()
ent_light5.kv.update(
    {
        'classname': 'light',
        'delay': '5',
        'wait': '.67',
        'light': '140',
    }
)
ent_light2.kv.update(
    {
        'classname': 'light',
        'delay': '2',
        'wait': '2.25',
        'light': '67',
        '_bounce': '-1',
    }
)


colors = {
    r'%rainbow_red': '#e31a0f',
    r'%rainbow_orange': '#f28a0f',
    r'%rainbow_yellow': '#efe61f',
    r'%rainbow_green': '#79b925',
    r'%rainbow_blue': '#2857a5',
    r'%rainbow_purple': '#6d1e81',
    r'%enby_yellow': '#fff42f',
    r'%enby_white': '#ffffff',
    r'%enby_purple': '#9c58d1',
    r'%enby_black': '#292929',
    r'%trans_blue': '#5bcffa',
    r'%trans_pink': '#f5aab9',
    r'%trans_white': '#ffffff',
    r'%bi_pink': '#d70071',
    r'%bi_purple': '#9c4e97',
    r'%bi_blue': '#0035a9',
    r'%dis_gray': '#595959',
    r'%dis_green': '#38b17e',
    r'%dis_blue': '#7cc3e1',
    r'%dis_white': '#e9e9e9',
    r'%dis_yellow': '#efdf78',
    r'%dis_red': '#d07381',
    r'%mlm5_1': '#078d70',
    r'%mlm5_2': '#98e8c1',
    r'%mlm5_3': '#ffffff',
    r'%mlm5_4': '#7bade2',
    r'%mlm5_5': '#3d1a78',
    r'%it_green': '#009344',
    r'%it_white': '#ffffff',
    r'%it_red': '#cf2734',
    r'%lava': '#ff4561',
    r'%mid': '#b689ff',
    r'%top': '#ff62b6',
    r'%tunnel': '#fff4e4',
}
for k, v in colors.items():
    colors[k] = hex_rgb(v)


def replace_texture(ent: Entity, a: str, b: str) -> None:
    for brush in ent.brushes:
        for face in brush.planes:
            if face.texture_name == a:
                face.texture_name = b


def setup_alarm_light(original: Entity) -> Entity:
    newlight = copy.deepcopy(original)
    newlight.kv.update(
        {
            '_color': '255 0 0',
            'targetname': 'quad_lights_red',
            'spawnflags': '1',
        }
    )
    return newlight


def main(input: list[Entity], context: dict) -> None:
    VAR_PREFIX: str = context['var_prefix']
    EVAL_PREFIX = VAR_PREFIX + 'eval'

    assert input[0].classname == 'worldspawn'
    add: list[Entity] = []
    add2: list[Entity] = []
    one_wall = Entity()
    one_wall.kv.update(
        {
            'classname': 'func_wall',
            '_shadow': '1',
        }
    )
    add.append(one_wall)

    for ent in input:
        # delete
        if ent.kv.get(VAR_PREFIX + 'delete') == '1':
            input.remove(ent)
            continue

        if ent.kv.get('_color') in colors:
            ent.kv['_color'] = colors[ent.kv['_color']]
        if ent.kv.get('_minlight_color') in colors:
            ent.kv['_minlight_color'] = colors[ent.kv['_minlight_color']]

        match ent.classname:
            case 'light':
                if ent.kv.get(VAR_PREFIX + 'lite') == '1':
                    dc = copy.deepcopy(ent)
                    dc.kv['delay'] = '2'
                    dc.kv['wait'] = '2.25'
                    dc.kv['light'] = '67'
                    dc.kv['_color'] = ent.kv.get('_color', '255 255 255')
                    dc.kv['_bounce'] = '-1'
                    add.append(dc)
            case 'info_null':
                if ent.kv.get(VAR_PREFIX + 'lite') == 'gen':
                    l2 = copy.deepcopy(ent_light2)
                    l5 = copy.deepcopy(ent_light5)
                    for light in [l2, l5]:
                        for key, val in ent.kv.items():
                            if key not in ['classname', 'angle', '@lite']:
                                light.kv[key] = val
                        add.append(light)

        for brush in ent.brushes:
            for face in brush.planes:
                match face.texture_name:
                    case '*lava8b' | '*tele128_blu1':
                        for coord in face.uv:
                            coord.offset = 0.0
                            coord.scale = 2.0
                    case 'floor_red_c':
                        face.texture_name = 'tch_c1_grey2'
                        for coord in face.uv:
                            coord.offset = 0.0

        # eval
        for key in ent.kv:
            if ent.kv[key].startswith(EVAL_PREFIX):
                ent.kv[key] = eval(ent.kv[key].removeprefix(EVAL_PREFIX))

        # replace proto textures
        for key in replace_proto:
            replace_texture(ent, key, replace_proto[key])

    input += add

    for ent in input:
        match ent.classname:
            case 'info_null':
                input.remove(ent)
            case 'light':
                if ent.kv.get('@noalarm') != '1':
                    ent.kv['targetname'] = 'quad_lights'
                    add2.append(setup_alarm_light(ent))

    input += add2

    # ---

    output = []

    for ent in input:
        # ezquake, fteqw
        # faces that overlap with fences get culled in the above engines
        if ent.classname == 'func_detail_fence':
            one_wall.brushes += ent.brushes
            continue
        else:
            output.append(ent)

    for ent in output:
        assert ent.classname != 'func_detail_fence'

    input.clear()
    input += output
