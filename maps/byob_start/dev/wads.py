import csv
import subprocess
from pathlib import Path

SUBMISSIONS = Path(Path(__file__).parent / r'..\mapsrc\BYOB - submissions.tsv')


# https://docs.python.org/3/library/csv.html
def read_csv() -> list[dict]:
    reader = csv.DictReader(SUBMISSIONS.read_text().splitlines(), delimiter='\t')
    obj = [row for row in reader]
    return obj


p_byob = Path(r'I:\byob')
p_wads = Path(p_byob / 'wads')
p_extracted = Path(p_byob / 'wads_extracted')
p_merged_wad = Path(p_byob / 'merged.wad')
p_renamed = Path(p_byob / 'renamed')
tools = [
    'clip',
    'skip',
    'trigger',
    'region',
    'antiregion',
    'slimeskip',
    'waterskip',
    'lavaskip',
]


tools2 = []
for tex in tools:
    fbr = tex + '_fbr'
    tools2.append(tex)
tools += tools2
del tools2


def extract():
    p_extracted.mkdir()
    for item in p_wads.iterdir():
        specific = p_extracted / item.stem
        specific.mkdir(exist_ok=True)
        subprocess.run(cwd=specific, args=['qpakman', '-extract', item])


def find_dupes():
    seen = set()
    dupes = set()
    for file in p_extracted.rglob('**/*.png'):
        slug = file.name
        if slug in seen:
            dupes.add(slug)
        else:
            seen.add(slug)
    print(dupes)


def do_it():
    for person in read_csv():
        pattern = person['WAD filename pattern'][:-4]
        if not pattern:
            continue

        for folder in p_extracted.iterdir():
            if not folder.match(pattern):
                continue
            i = 0
            for file in folder.iterdir():
                new_name = f'{person["nickname"][:4].lower()}_{i:03}'

                if file.stem.endswith('_fbr'):
                    new_name += '_fbr'

                if file.stem.startswith('star_'):
                    new_name = 'star_' + new_name
                elif file.stem.startswith('plus_'):
                    new_name = 'plus_' + file.stem[5] + new_name
                elif file.stem.startswith('_') and file.stem.endswith('_fbr'):
                    new_name = '{' + new_name

                file.copy(p_renamed / (new_name + file.suffix))
                i += 1


def pack():
    subprocess.run(['qpakman', str(p_renamed) + r'\*', '-o', p_merged_wad])
