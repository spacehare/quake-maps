from pathlib import Path
from subprocess import run

parent = Path(__file__).parent.absolute()
textures = parent.parent / 'textures' / 'mcj2_rabbit'
temp = parent / 'temp'
qpakman = parent / 'qpakman'

textures.mkdir(exist_ok=True, parents=True)
temp.mkdir(exist_ok=True)
qpakman.mkdir(exist_ok=True)


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
    # terracotta
    'black_glazed_terracotta': 'terra_black',
    'blue_glazed_terracotta': 'terra_blue',
    'brown_glazed_terracotta': 'terra_brown',
    'cyan_glazed_terracotta': 'terra_cyan',
    'gray_glazed_terracotta': 'terra_gray',
    'green_glazed_terracotta': 'terra_green',
    'light_blue_glazed_terracotta': 'terra_lblue',
    'light_gray_glazed_terracotta': 'terra_lgray',
    'lime_glazed_terracotta': 'terra_lime',
    'magenta_glazed_terracotta': 'terra_magenta',
    'orange_glazed_terracotta': 'terra_orange',
    'pink_glazed_terracotta': 'terra_pink',
    'purple_glazed_terracotta': 'terra_purple',
    'red_glazed_terracotta': 'terra_red',
    'white_glazed_terracotta': 'terra_white',
    'yellow_glazed_terracotta': 'terra_yellow',
    # frog lights
    'ochre_froglight_side': 'frog_ochre_s',
    'ochre_froglight_top': 'frog_ochre_t',
    'pearlescent_froglight_side': 'frog_pearl_s',
    'pearlescent_froglight_top': 'frog_pearl_t',
    'verdant_froglight_side': 'frog_verdant_s',
    'verdant_froglight_top': 'frog_verdant_t',
    # lanterns
    'lantern': '{lantern_fbr',
    'soul_lantern': '{lantern_soul_fbr',
    # text
    'ascii': '{ascii_fbr',
    'ascii_invert': '{ascii_invert_fbr',
    '': '',
}


# clean up previous run
for folder in [textures, temp, qpakman]:
    for file in folder.iterdir():
        file.unlink()


# convert
run(
    f'magick mogrify -scale 200% -format tga -compress rle -path {temp} rip/*.png'.split(),
    cwd=parent,
)

# rename files
for file in temp.iterdir():
    if file.stem in stems_dict:
        file.rename(file.with_stem(stems_dict[file.stem]))

# trans
run(
    f'magick mogrify -background #9F5B53 -alpha remove -path {qpakman} temp/*.tga'.split(),
    cwd=parent,
)

# qpakman
run(
    rf'qpakman {qpakman}/*.tga -o I:\Quake\wads\per-map\mcj2_rabbit.wad'.split(),
    cwd=parent,
)

# optimize file sizes
run(
    f'magick mogrify -alpha off-if-opaque -path {textures} temp/*.tga'.split(),
    cwd=parent,
)

# clean up external texture names
for file in textures.iterdir():
    file.rename(file.with_stem(file.stem.removesuffix('_fbr')))
