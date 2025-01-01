- [map source on github](https://github.com/spacehare/quake-maps/tree/main)

# tools used

- [TrenchBroom 2024.2](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)

## compile settings

| tool  | args                                                                                |
| ----- | ----------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -splitturb -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                    |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

# credit

# DON'T WORRY — BE FURRY
