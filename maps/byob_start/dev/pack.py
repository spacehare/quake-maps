import shutil
import subprocess
from pathlib import Path

p_dir = Path(r'I:\byob')
p_submissions = p_dir / 'submissions'
p_wads = p_dir / 'wads'
p_mod = Path(r'I:\Quake\Game\engines\byob')
p_copper = p_dir / 'copper1.35_base'
parent = Path(__file__).parent

other_files = [
    parent / 'descript.ion',
    p_dir / 'readme.md',
    p_dir / 'readme.html',
]

whitelist_pairs = {
    '**/*.bsp': 'maps',
    '**/*.lit': 'maps',
    '**/*.map': 'mapsrc',
    '**/*.py': 'mapsrc',
    '**/*.txt': 'readmes',
    '**/*.md': 'readmes',
    '**/*.html': 'readmes',
    '**/*.wad': 'wads',
    '**/*.mdl': 'progs',
    '**/gfx/env/*': 'gfx/env',
    '**/sound/*': 'sound',
    '**/track*.*': 'music',
}


def compress_skies():
    for item in p_mod.rglob('gfx/env/**'):
        if item.is_file():
            assert item.suffix == '.tga'
            subprocess.run(['magick', 'mogrify', '-compress', 'rle', '-alpha', 'off', '-type', 'TrueColor', str(item)])

            for glob_match in p_submissions.rglob('**/' + item.name):
                glob_match_size = glob_match.stat().st_size
                item_size = item.stat().st_size

                if glob_match_size < item_size:
                    print(glob_match_size, '<', item_size)
                    item.unlink()
                    glob_match.copy(item)


def copy_files():
    p_mod.mkdir(exist_ok=False)
    mod_wads = p_mod / 'wads/'
    mod_wads.mkdir(parents=True)

    # copy misc
    for file in other_files:
        print('other file:', file)
        file.copy(p_mod / file.name)

    # copy wads
    for wad in p_wads.iterdir():
        print('wad:', wad)
        wad.copy(mod_wads / wad.name, preserve_metadata=True)

    # iterate through submission files
    for pattern, dest_string in whitelist_pairs.items():
        p_destination = p_mod / Path(dest_string)
        p_destination.mkdir(parents=True, exist_ok=True)

        for item in p_submissions.rglob('*'):
            is_match = item.full_match(pattern)
            if is_match:
                print(p_destination / item.name)
                item.copy(p_destination / item.name, preserve_metadata=True)

    for item in p_copper.iterdir():
        item.copy_into(p_mod)


def rename_files():
    rename = {
        'byob_start.bsp': 'start.bsp',
        'byob_start.lit': 'start.lit',
        'byob_start.md': 'start.md',
        'byob_start.html': 'start.html',
    }

    for file in p_mod.rglob('*'):
        for k, v in rename.items():
            if file.name == k:
                file.rename(file.with_name(v))


def clean_up():
    shutil.rmtree(p_mod / 'autosave')
    for item in p_mod.iterdir():
        if item.match('*.cfg'):
            item.unlink()
