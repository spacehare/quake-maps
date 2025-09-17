- the map source is included in the files, [but it's also on github!](https://github.com/spacehare/quake-maps)
  - when you see "@clip 1" in any entity, it's for a python script i use to add clip brushes to `func_detail_illusionary` entities

# tools used

- [TrenchBroom 2025.3](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha9-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha9)
- [MESS 1.2.3](https://pwitvoet.github.io/mess/)

## compile settings

| tool  | args                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -litwater -bsp2 ${WORK_DIR_PATH}/build/__${MAP_BASE_NAME}__BUILD.map maps/${MAP_BASE_NAME}.bsp` |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                                           |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                        |

# credit

- music: "On Your Feet" by Frank Klepacki, from "Command & Conquer: Renegade"
- button sound: `mousedown2.wav` from Starcraft: Brood War
- [Rabbit Emoji](https://github.com/googlefonts/noto-emoji/blob/main/svg/emoji_u1f407.svg)
- [skybox](https://www.slipseer.com/index.php?resources/tga-conversion-of-bumbadidas-skyboxes.481/) by bumbadida

# DON'T WORRY — BE FURRY
