- [map source also on github](https://github.com/spacehare/quake-maps)

# tools used

- MAPPING: [TrenchBroom-Win64-AMD64-v2025.3-Release](https://trenchbroom.github.io/)
- COMPILING: [ericw-tools-2.0.0-alpha10-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha10)
<!-- - MUSIC: [OpenMPT 1.31.10.00](https://openmpt.org/) -->

## compile settings

| tool  | args                                                                               |
| ----- | ---------------------------------------------------------------------------------- |
| QBSP  | `-leaktest -litwater -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`   |
| VIS   | `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`                   |
| LIGHT | `-extra -emissivequality high -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp` |

### compile times

- qbsp: 34.379s seconds elapsed
- vis: 237.58s elapsed
- light: 41082.832s seconds elapsed

# credit

  <!-- - track255 by me and twofold, made in OpenMPT
  - twofold
    - https://2xtwofold.bandcamp.com
    - https://soundcloud.com/2xtwofold
  - sounds from
    - [msx.horse](https://msx.horse/), and msx [instrument library](https://github.com/msx2plus/msx_iti_collection/tree/main)
    - A 'footstep on wood' sound from the original Sam & Max 100 series games
    - some half-life 2 concrete noises -->

- track255: Crystal Formations, by Realm of Mind (apterous)
  - from [Runic Resonances](https://www.slipseer.com/index.php?resources/quake-music-jam-1-runic-resonances.292/)
- some sfx from Half Life
- [most textures by Makkon](https://www.slipseer.com/index.php?resources/makkon-textures.28/)
  - some textures modified by me (in 2022)
- thanks to RadiatorYang, for sending the connifer tree texture
- other foliage textures (vines, grass) via the quake discord
- water textures from liquids.WAD via https://www.quaddicted.com/files/wads/
- skybox = [Overcast](https://gamebanana.com/mods/380496)
  - converted to .PNG in VIDE, then to .TGA in IrfanView (this was done in 2022 during the original QBJ)
  - also scaled down by 50% using ImageMagick (in 2025, because the file sizes were fucking huge at 2048x2048)

# notes, changes

- WADs were updated to the modern Makkon concrete textures
- fixed the softlocks on Skill 0
- some minor geo/brushwork changes, added `_phong` to some brushes, etc
- refactored all the entities (enemies, weapons, armor, ammo, etc)
- altered some secrets

# DON'T WORRY — BE FURRY
