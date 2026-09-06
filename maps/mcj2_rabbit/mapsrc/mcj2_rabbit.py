# this Python file contains code to process the MAP file at compile time
# it runs after MESS, and before ericw-tools

# https://github.com/spacehare/rabbit_quake

from rabbitquake.app.parse import Entity

dont_reset = [
    'banners',
]


def main(input: list[Entity], context: dict) -> None:
    for ent in input:
        for brush in ent.brushes:
            for plane in brush.planes:
                if plane.texture_name in dont_reset:
                    continue
                plane.rotation = 0.0
                for axis in plane.uv:
                    axis.offset = 0.0
                    axis.scale = 0.0
                    for vert in axis.point:
                        vert = abs(vert)

        for key in ent.kv:
            if ent.kv[key].startswith('eval'):
                ent.kv[key] = eval(ent.kv[key].removeprefix('eval'))
