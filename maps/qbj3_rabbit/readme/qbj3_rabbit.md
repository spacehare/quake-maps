- the map source is included in the files, [but it's also on github!](https://github.com/spacehare/quake-maps)

# tools used

- [TrenchBroom 2025.3](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha10-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha10)
- [MESS 1.2.3](https://pwitvoet.github.io/mess/)
- [Krita 5.2.13](https://krita.org/en/)
- Python 3.13.7
  - [some of my own jank scripts](https://github.com/spacehare/rabbit_quake), like `pp.py` (pre-processor)

## TrenchBroom compile steps and arguments

| tool   | args                                                                                                                                                      |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Export | `${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map`                                                                                                    |
| MESS   | `-config quake ${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map`                                                                                      |
| pp.py  | `${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map ${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map ${WORK_DIR_PATH}/mapsrc/${MAP_BASE_NAME}.yaml` |
| QBSP   | `-leaktest -litwater -bsp2 ${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map maps/${MAP_BASE_NAME}.bsp`                                                |
| VIS    | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                                                                                          |
| LIGHT  | `-extra -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                                                                        |

### compile times

- qbsp: 30.054s seconds elapsed
- vis: 67.21s elapsed
- light: 42077.130s seconds elapsed

# credit

- [textures by makkon](https://www.slipseer.com/index.php?resources/makkon-textures.28)
- sky from [these TGA skies i converted from PNG, by bumbadida](https://www.slipseer.com/index.php?resources/tga-conversion-of-bumbadidas-skyboxes.481/) -- and again converted to grayscale TGA using ImageMagick
- decals/graffiti by me
- music by twofold
  - https://2xtwofold.bandcamp.com
  - https://soundcloud.com/2xtwofold
  - using Ableton Live

## media inspiration

- Silksong
- Hazbin Hotel
- Halo
- Half Life 2
- H3VR Take & Hold Institution
- Junk Head
- Total Recall

## Thank you for design feedback

- makkon
- avix
- stickflip
- sze

## Thank you for playtesting

- alexUnder (no surname, just Alex like Moses)
- b0rdie
- clenow
- spootnik
- avix (worlds #1 family guy fan)
- softi
- wons (white eminem theorist)
- awakeralex
- milestone

# misc

OCs (original characters) featured in art decals:

- Io, the space hare (they/them/their, it/it/its); fursona
- Zifix, the cave goblin (they/them/their); goblin-sona
- Oolo, the imp (ey/em/eir, e/em/eir); imp-sona
- The Monster (it/it/its); monster-sona
  - i still haven't come up with a name yet lol
- Moss, the night fury (they/them/their); HTTYD OC

Other symbols include

- Toki Pona writing (sitelen pona)
- Therian symbol
- Otherkin symbol
- Alterhuman symbol

# DON'T WORRY — BE FURRY
