from pathlib import Path
from subprocess import run

in_folder = Path(r'I:\Quake\skies')
out_folder = Path(r'I:\Quake\skies\out')

if not out_folder.exists():
    out_folder.mkdir()

conv = {
    'bumbadida_cyan_': '20250701_164506_0706_',
    'bumbadida_gray_': '20250617_202114_0436_',
    'bumbadida_dark_': '20250627_213710_0671_',
    'bumbadida_cloudy_': '20250530_174917_0313_',
    'mak_purplesky4_': 'mak_purplesky4_',
    'mak_purplesky5_': 'mak_purplesky5_',
    'mak_purplesky6_': 'mak_purplesky6_',
    'mak_sunset1_': 'mak_sunset1_',
}

for path in in_folder.rglob('*'):
    for key_new_name, path_stem_start in conv.items():
        if path.stem.startswith(path_stem_start):
            print('-> %s' % path)
            for effect in ['gray', 'mod']:
                out_file = (out_folder / (effect + '_' + key_new_name + path.stem[-3:])).with_suffix('.tga')
                print('\t', out_file)
                args: list[str] = []

                if effect == 'gray':
                    args = ['-colorspace', 'gray']
                elif effect == 'mod':
                    args = ['-modulate', '100,25,100']
                run(['magick', str(path), *args, out_file])
