import argparse
from copy import deepcopy
from pathlib import Path

import pyperclip
from rabbitquake.app.parse import Brush, Entity

atlas_path = Path(__file__).parent / './atlas_flamboyant.txt'
brush_path = Path(__file__).parent / './brush.txt'
splitted = [line.split() for line in atlas_path.read_text().splitlines()]
brush_letter: Brush = Entity.loads(brush_path.read_text()).brushes[0]

atlas_dict: dict[str, tuple[int, int]] = {}

TEXTURENAME_SRC = 'hub_flamboyant'
TEXTURENAME_NEW = '{hub_flamboyant'
ENT_CLASS = 'func_detail_illusionary'

for y, row in enumerate(splitted):
    for x, char in enumerate(row):
        atlas_dict[char] = (x, y)

atlas_dict[' '] = (15, 7)


def shift(brush: Brush, size: int, idx: int, x: int, y: int, height: int) -> None:
    for plane in brush.planes:
        if plane.texture_name == TEXTURENAME_SRC:
            plane.texture_name = TEXTURENAME_NEW
            plane.uv.u.offset = float((x - idx) * size)
            plane.uv.v.offset = float((y - height) * size)
        for point in plane.points:
            point.x += size * idx
            point.z -= size * height


def write(text: str) -> Entity:
    text = text.replace('\\n', '\n')
    lines = text.splitlines()
    out: Entity = Entity()
    out.kv['classname'] = ENT_CLASS
    for height, line in enumerate(lines):
        for idx, char in enumerate(line):
            coord = atlas_dict[char]
            clone = deepcopy(brush_letter)
            brush_size = 8
            shift(clone, brush_size, idx, coord[0], coord[1], height)
            out.brushes.append(clone)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('text', type=str)
    args = ap.parse_args()
    pyperclip.copy(write(args.text).dumps())
