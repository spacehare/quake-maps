import subprocess
from pathlib import Path

p_dir = Path(r'I:\byob')
p_submissions = p_dir / 'submissions'
p_wads = p_dir / 'wads'
p_mod = Path(r'I:\Quake\Game\engines\byobtest')
p_copper = p_dir / 'copper1.35_base'

whitelist_pairs = {
    '**/*.bsp': 'maps',
    '**/*.lit': 'maps',
    '**/*.map': 'mapsrc',
    '**/*.txt': '_extras/readmes',
    '**/*.md': '_extras/readmes',
    '**/*.html': '_extras/readmes',
    '**/*.wad': '_extras/wads',
    '**/*.mdl': 'progs',
    '**/gfx/env/*': 'gfx/env',
    '**/sound/*': 'sound',
    '**/track*.*': 'music',
}


def compress_skies():
    for item in p_mod.rglob('gfx/env/**'):
        if item.is_file():
            assert item.suffix == '.tga'
            subprocess.run(['magick', 'mogrify', '-compress', 'rle', '-alpha', 'off', str(item)])

            for glob_match in p_submissions.rglob('**/' + item.name):
                glob_match_size = glob_match.stat().st_size
                item_size = item.stat().st_size

                if glob_match_size < item_size:
                    print(glob_match_size, '<', item_size)
                    item.unlink()
                    glob_match.copy(item)


def main():
    p_mod.mkdir(exist_ok=False)

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


main()
compress_skies()
