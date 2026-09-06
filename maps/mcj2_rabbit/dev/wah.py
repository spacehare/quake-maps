from pathlib import Path
from subprocess import run

parent = Path(__file__).parent
textures = parent.parent / 'textures' / 'mcj2_rabbit'

if not textures.exists():
    textures.mkdir(parents=True)


stems_dict = {
    'mushroom_block_inside': 'mush_inside',
    'mushroom_stem': 'mush_stem',
    'red_mushroom_block': 'mush_red',
    'brown_mushroom_block': 'mush_brown',
    'redstone_lamp': '+0rs_lamp',
    'redstone_lamp_on': '+1rs_lamp',
    # quartz
    'quartz_block_bottom': 'quartz_bot',
    'quartz_block_side': 'quartz_side',
    'quartz_block_top': 'quartz_top',
    'quartz_bricks': 'quartz_brick',
    'quartz_pillar': 'quartz_pil',
    'quartz_pillar_top': 'quartz_pil_top',
    'chiseled_quartz_block': 'quartz_chi',
    'chiseled_quartz_block_top': 'quartz_chi_top',
    '': '',
}

#  clean the directory
for file in textures.iterdir():
    file.unlink()

# ImageMagick
run(
    rf'magick mogrify -scale 200% -format tga -alpha off -type TrueColor -compress rle -path {textures.absolute()} rip/*.png'.split(),
    cwd=parent,
)

# rename files
for file in textures.iterdir():
    if file.stem in stems_dict:
        file.rename(file.with_stem(stems_dict[file.stem]))

# qpakman
run(
    rf'qpakman {textures.absolute()}/*.tga -o I:\Quake\wads\per-map\mcj2_rabbit.wad'.split(),
    cwd=parent,
)
