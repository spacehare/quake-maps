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
