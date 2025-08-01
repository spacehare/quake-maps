- the map source is included in the files, [but it's also on github!](https://github.com/spacehare/quake-maps)

# tools used

- [TrenchBroom 2025.3](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)

## compile settings

| tool  | args                                                                                              |
| ----- | ------------------------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -litwater -bsp2 ${WORK_DIR_PATH}/build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp` |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                                  |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`               |

# credit

- track255 made by me in OpenMPT 1.31.10.00
  - music/instrument SFX (for doors and trains) from [msx.horse](https://msx.horse)
  - music made with samples from [msx.horse](https://msx.horse) and Half Life 2
- "kerclunk" button sound from my friend
- "bachu" button sound from another friend
- prototype textures from [LibreQuake](https://github.com/lavenderdotpet/LibreQuake)
- hazard stripe texture by me, made in Krita
- [Rabbit Emoji](https://github.com/googlefonts/noto-emoji/blob/main/svg/emoji_u1f407.svg)

# notes

wow. `func_door`s and `func_train`s are REALLY easy to desync, huh.

# DON'T WORRY — BE FURRY
