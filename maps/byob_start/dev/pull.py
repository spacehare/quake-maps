from pathlib import Path

from rabbitquake.app.bsp import read_bsp

p_dir = Path(r'I:\byob')
p_submissions = p_dir / 'submissions'
p_wads = p_dir / 'wads'


for item in p_submissions.rglob('**'):
    if item.is_file() and item.suffix == '.bsp':
        print(item)
        worldspawn = read_bsp(item).entities[0]
        print(worldspawn.kv.get('message'))
