- [map source also on github](https://github.com/spacehare/quake-maps)

# tools used

- MAPPING: [TrenchBroom-Win64-AMD64-v2025.1-Release](https://trenchbroom.github.io/)
- COMPILING: [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)
- MUSIC: [OpenMPT 1.31.10.00](https://openmpt.org/)

## compile settings

| tool  | args                                                                                |
| ----- | ----------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -splitturb -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                    |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

# credit

- track255 by me, made in OpenMPT using sounds from [msx.horse](https://msx.horse/)
- sfx from minecraft, some i converted from OGG to WAV using ffmpeg and a python script. others provided by Avix, the jam host
- skybox provided by steam_the_2nd in the quake mapping discord, which i converted from PNG to TGA using IrfanView

# random notes

- i suddenly got motivation to do the last 90% of this map during the last 12 hours lmfao
- things i listened to for background noise while mapping
  - altabiscuit's DK64 randomizer VODs
  - Proto Pabz ASMR
  - minecraft OST

# DON'T WORRY — BE FURRY
