# this Python file contains code to pre-process the MAP file

# https://github.com/spacehare/rabbit_quake


import copy


def clip(ent) -> list:
    output_brushes: list = []
    for brush in ent.brushes:
        clone = copy.deepcopy(brush)
        for plane in clone.planes:
            plane.texture_name = 'clip'
        output_brushes.append(clone)
    return output_brushes


def main(context: dict) -> list:
    print('🐇 running qbj3_rabbit.py')

    var_prefix = context['var_prefix']
    input_entities = context['entities']
    output_entities: list = []

    print('prefix: %s' % var_prefix)

    assert input_entities[0].classname == 'worldspawn'

    worldspawn = input_entities[0]

    for ent in input_entities:
        if ent.kv.get(var_prefix + 'delete') == '1':
            continue
        else:
            output_entities.append(ent)

        for key in ent.kv:
            if ent.kv[key].startswith('eval'):
                ent.kv[key] = eval(ent.kv[key].removeprefix('eval'))

        classname: str = ent.kv['classname']

        if ent.kv.get(var_prefix + 'clip') == '1':
            worldspawn.brushes += clip(ent)

        # door
        if classname == 'func_door':
            ent.kv.setdefault('_minlight', '50')
            ent.kv.setdefault('sounds', '3')
            ent.kv.setdefault('_dirt', '-1')

        # purge angles
        if (
            classname.startswith('trigger')
            and not ent.kv.get(var_prefix + 'use_angle') == '1'
            and ent.kv.get('angle')
            and not classname.endswith('monsterjump')
        ):
            print('clearing angle on %s' % classname)
            del ent.kv['angle']

        # texture swapping
        if tex := ent.kv.get(var_prefix + 'replace_texture_from'):
            for brush in ent.brushes:
                for face in brush.planes:
                    if face.texture_name == tex:
                        face.texture_name = ent.kv[var_prefix + 'replace_texture_with']

    return output_entities
