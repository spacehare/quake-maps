from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from rabbitquake.app import bsp

folder = Path(r'I:\byob\submissions')
outputfile = Path(r'I:\byob\monsterdata.csv')


def get_skills(spawnflags: int):
    is_easy = not (Skillsflags.NOT_ON_EASY.value & spawnflags)
    is_normal = not (Skillsflags.NOT_ON_NORMAL.value & spawnflags)
    is_hard = not (Skillsflags.NOT_ON_HARD.value & spawnflags)

    return is_easy, is_normal, is_hard


class Skillsflags(Enum):
    NOT_ON_EASY = 256  # '0b00100000000'
    NOT_ON_NORMAL = 512  # '0b01000000000'
    NOT_ON_HARD = 1024  # '0b10000000000'


@dataclass
class Monster:
    classname: str
    easy_count: int
    norm_count: int
    hard_count: int


maps: dict[str, list[Monster]] = {}
for bspfile in folder.rglob('*.bsp'):
    bspdata = bsp.read_bsp(bspfile)
    map_monsters = []
    for ent in bspdata.entities:
        if ent.classname.startswith('monster'):
            monster = Monster(ent.classname, 0, 0, 0)
            spawnflags = ent.kv.get('spawnflags') or 0
            easy, norm, hard = get_skills(int(spawnflags))
            count = ent.kv.get('count')
            count = int(count) if count else 1
            if easy:
                monster.easy_count += 1 * count
            if norm:
                monster.norm_count += 1 * count
            if hard:
                monster.hard_count += 1 * count
            map_monsters.append(monster)
    maps[bspfile.stem] = map_monsters


monster_strings = [
    'army',
    'boss',
    'demon1',
    'dog',
    'enforcer',
    'fish',
    'hell_knight',
    'knight',
    'ogre',
    'oldone',
    'shalrath',
    'shambler',
    'tarbaby',
    'wizard',
    'zombie',
]
monster_strings = [f'monster_{s}' for s in monster_strings]

table = ',,'
table += ','.join(monster_strings) + '\n'

for stem, monsters_list in maps.items():
    totals: dict[str, list[int]] = {}
    for classname in monster_strings:
        totals[classname] = [0, 0, 0]
        for mon in monsters_list:
            if mon.classname == classname:
                totals[classname][0] += mon.easy_count
                totals[classname][1] += mon.norm_count
                totals[classname][2] += mon.hard_count
    print(totals)
    table += f'{stem},easy,' + ','.join([str(v[0]) for k, v in totals.items()]) + '\n'
    table += f'{stem},normal,' + ','.join([str(v[1]) for k, v in totals.items()]) + '\n'
    table += f'{stem},hard,' + ','.join([str(v[2]) for k, v in totals.items()]) + '\n'

outputfile.write_text(table)
