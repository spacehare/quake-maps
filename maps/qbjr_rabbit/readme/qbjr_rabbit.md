- [map source also on github](https://github.com/spacehare/quake-maps)

# tools used

- MAPPING: [TrenchBroom-Win64-AMD64-v2025.3-Release](https://trenchbroom.github.io/)
- COMPILING: [ericw-tools-2.0.0-alpha10-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha10)
- MUSIC: [OpenMPT 1.31.10.00](https://openmpt.org/)

## compile settings

| tool  | args                                                                               |
| ----- | ---------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -litwater -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                   |
| LIGHT | `-extra -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

# credit

- track255 by me and twofold, made in OpenMPT
  - twofold
    - https://2xtwofold.bandcamp.com
    - https://soundcloud.com/2xtwofold
  - sounds from
    - [msx.horse](https://msx.horse/)
    - A 'footstep on wood' sound from the original Sam & Max 100 series games
    - some half-life 2 concrete noises
- some sfx from Half Life
- most textures by Makkon
  - some textures modified by me (in 2022)
- foliage textures from the quake discord
- water textures from liquids.WAD via https://www.quaddicted.com/files/wads/
- skybox = Overcast https://gamebanana.com/mods/380496
  - converted to .PNG in VIDE, then to .TGA in IrfanView (this was done in 2022 during the original QBJ)
  - also scaled down by 50% using ImageMagick

# notes, changes

- WADs were updated to the modern Makkon concrete textures
- fixed the softlocks on Skill 0
- some minor geo/brushwork changes
- refactored all the entities (enemies, weapons, armor, ammo, etc)
- altered some secrets

# DON'T WORRY — BE FURRY
