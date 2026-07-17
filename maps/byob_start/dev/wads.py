import subprocess
from pathlib import Path

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

stuff = {
    'auh_dev': 'auh_dev',
    'auh_liquids': 'auh_liq',
    'auh_nature': 'auh_nat',
    'auh_skies': 'auh_ski',
    'auh_tools': 'auh_too',
    'auh_walls': 'auh_wal',
    'byobchumastic': 'chum',
    'byob_4lt': '4lt',
    'byob_avix': 'avix',
    'byob_cc': 'cc',
    'byob_chaosed0': 'chao',
    'byob_chaosed0_tool': 'chao_too',
    'byob_dicedpinecones': 'diced',
    'byob_EHOT': 'ehot',
    'byob_gnorlio': 'gnor',
    'byob_haikids': 'haik',
    'byob_naitelveni': 'nait',
    'byob_novafrost': 'nova',
    'byob_pm': 'pm',
    'byob_puppluka_lauravix': 'pupp',
    'byob_rabbit': 'rabb',
    'byob_rabbit_dev': 'rabb_dev',
    'byob_rabbit_proto': 'rabb_pro',
    'byob_redeadita': 'rede',
    'byob_roj': 'roj',
    'byob_squidv': 'squi',
    'byob_wons': 'wons',
    'chornobyl': 'rory',
    'crayons1': 'quie',
    'library': 'clen',
    'moko': 'moko',
    'razzzor_tex': 'razz',
    'shinko_zed666': 'shin',
}


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


def rename_textures():
    p_renamed.mkdir()
    for k, v in stuff.items():
        folder = p_extracted / k
        i = 0
        for file in folder.iterdir():
            new_name = f'{v}_{i:03}'

            if file.stem.endswith('_fbr'):
                new_name += '_fbr'

            if file.stem.startswith('star_'):
                file.copy(p_renamed / (new_name + file.suffix))
                new_name = 'star_' + new_name
            elif file.stem.startswith('plus_'):
                new_name = 'plus_' + file.stem[5] + new_name
            elif file.stem.startswith('_') and file.stem.endswith('_fbr'):
                new_name = '{' + new_name

            file.copy(p_renamed / (new_name + file.suffix))
            i += 1


def pack():
    subprocess.run(['qpakman', str(p_renamed) + r'\*', '-o', p_merged_wad])
