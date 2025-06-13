- [map source also on github](https://github.com/spacehare/quake-maps)

# tools used

- MAPPING: [TrenchBroom-Win64-AMD64-v2025.3-Release](https://trenchbroom.github.io/)
- COMPILING: [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)
- MUSIC: [OpenMPT 1.31.10.00](https://openmpt.org/)

## compile settings

| tool  | args                                                                                |
| ----- | ----------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -splitturb -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                    |
| LIGHT | `-extra4 -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

# credit

- track255 by me, made in OpenMPT
  - sounds from [msx.horse](https://msx.horse/)
  - also used a 'footstep on wood' sound from the original Sam & Max 100 series games
- some sfx from Half Life
- most textures by Makkon
  - some textures modified by me (in 2022)
- foliage textures from the quake discord
- water textures from liquids.WAD via https://www.quaddicted.com/files/wads/
- skybox = Overcast https://gamebanana.com/mods/380496
  - converted to .PNG in VIDE, then to .TGA in IrfanView (this was done in 2022 during the original QBJ)

# notes, changes

- WADs were updated to the modern Makkon concrete textures
- fixed the softlocks on Skill 0
- some minor geo/brushwork changes
- refactored all the entities (enemies, weapons, armor, ammo, etc)
- altered some secrets
- there is a bug present where you will end up with more kills than the max kill count. you might see 257/250 kills. i think this is a bug with the mod? or something? i don't know how to fix it, at least

# DON'T WORRY — BE FURRY
