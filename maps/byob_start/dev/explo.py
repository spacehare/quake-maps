from pathlib import Path

from rabbitquake.app import bsp

folder = Path(r'I:\byob\submissions')

for bspfile in folder.rglob('*.bsp'):
    data = bsp.read_bsp(bspfile)
    for ent in data.entities:
        if ent.classname.startswith('misc_explobox'):
            print(bspfile, ent.classname)
