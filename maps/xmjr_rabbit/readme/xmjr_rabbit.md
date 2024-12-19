- [map source on github](https://github.com/spacehare/quake-maps/tree/main)

# tools used

- [TrenchBroom 2024.2-RC1](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)

## compile settings

| tool  | args                                                                                |
| ----- | ----------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -splitturb -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                    |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

# credit

- skybox is "Dream Weavers" from Spyro 1, made into a quake-compatible skybox using Blender and Python (bpy)
- textures from LibreQuake and [Khreathor's prototype textures pack](https://www.slipseer.com/index.php?resources/prototype-wad.263/)
- track255 by... me!
  - made using `ITI`s from [this repo](https://github.com/msx2plus/msx_iti_collection) (via [msx.horse](https://msx.horse/))
    - and also the siege tank attack sound from Starcraft 1
  - i learned OpenMPT — or rather, i re-learned it. vaguely around a decade ago, i tried to make music with it and gave up. "i can't do this" i thought. but i tried again! and made something! it's kinda rough, i have no musical training, but hey, i made some music!!
- [Rabbit Emoji](https://github.com/googlefonts/noto-emoji/blob/main/svg/emoji_u1f407.svg)
- Pomni drawing by me, made in Krita

# DON'T WORRY — BE FURRY
