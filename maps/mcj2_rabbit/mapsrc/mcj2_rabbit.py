# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake

from rabbitquake.app.parse import Brush, Entity

dont_reset = [
    'banners',
    'wool_woke',
    'bone_side',
    'mush_stem',
    'log_birch',
    'basalt_side',
    'frog_pearl_s',
    'frog_verdant_s',
    'frog_ochre_s',
    '{lever',
    '{lantern',
    '{lantern_soul',
    'sign',
    '{ascii',
    '{ascii_invert',
]


def froggify(group: Entity, ent: Entity):
    newbrushes: list[Brush] = []

    for brush in ent.brushes:
        for plane in brush.planes:
            if brush in group.brushes:
                continue

            if plane.texture_name.startswith('frog'):
                group.brushes.append(brush)

            else:
                newbrushes.append(brush)

    ent.brushes.clear()
    ent.brushes += newbrushes


def main(input: list[Entity], context: dict) -> None:
    frog_group = Entity()
    frog_group.kv['classname'] = 'func_group'
    frog_group.kv['_minlight'] = '255'
    frog_group.kv['_lightignore'] = '1'

    score: int = 0
    vecs = [
        ((0.0, -1.0, 0.0), (0.0, 0.0, -1.0)),
        ((1.0, 0.0, 0.0), (0.0, 0.0, -1.0)),
        ((-1.0, 0.0, 0.0), (0.0, -1.0, 0.0)),
        ((1.0, 0.0, 0.0), (0.0, -1.0, 0.0)),
        ((-1.0, 0.0, 0.0), (0.0, 0.0, -1.0)),
        ((0.0, 1.0, 0.0), (0.0, 0.0, -1.0)),
    ]
    # FIXME
    # ericw alpha 11:
    # WARNING: ... repairing invalid texture projection ("wool_pink" near 704 -1152 -704)

    for ent in input:
        # delete
        if ent.kv.get('@delete') == '1':
            input.remove(ent)
            continue

        froggify(frog_group, ent)

        for brush in ent.brushes:
            for plane, numbers in zip(brush.planes, vecs):
                if plane.texture_name in dont_reset:
                    continue

                plane.rotation = 0.0

                for axis in plane.uv:
                    axis.offset = 0.0
                    axis.scale = 1.0

                plane.uv.u.point.x = numbers[0][0]
                plane.uv.u.point.y = numbers[0][1]
                plane.uv.u.point.z = numbers[0][2]
                plane.uv.v.point.x = numbers[1][0]
                plane.uv.v.point.y = numbers[1][1]
                plane.uv.v.point.z = numbers[1][2]

        for key in ent.kv:
            if ent.kv[key].startswith('eval'):
                ent.kv[key] = eval(ent.kv[key].removeprefix('eval'))

        match ent.classname:
            case 'item_score':
                score += 1000 if ent.kv.get('spawnflags') == '1' else 100

            case 'trigger_teleport':
                # X (RED)
                # Y (GREEN)
                # Z (BLUE) UP
                extend = 0.25
                for idx, plane in enumerate(ent.brushes[0].planes):
                    for pt in plane.points:
                        match idx:
                            case 0:
                                pt.x -= extend
                            case 1:
                                pt.y -= extend
                            case 2:
                                pt.z -= extend
                            case 3:
                                pt.z += extend
                            case 4:
                                pt.y += extend
                            case 5:
                                pt.x += extend

    for e in input:
        if e.kv.get('targetname') == 'scorecheck':
            e.kv['score'] = str(score)

    print('score:', score)

    input.append(frog_group)


# i'm the best programmer ever
