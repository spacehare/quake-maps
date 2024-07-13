# info

- stem: bonk_rabbit
- message: "Twitchy Tail Temple"
- by: rabbit
- mod: bonk
- host: spootnik
- version: 1
- made with: TrenchBroom-Win64-v2024.1-Release
- tested with: quakespasm 0.95, ironwail 0.7.0
- compiled with:
  - tool: ericw-tools-2.0.0-alpha7-win64
  - args:
    - qbsp: `-leaktest -splitturb -bsp2 mapsrc/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`
    - vis: `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`
    - light: `-extra4 -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`

# credit

textures:

- [makkon textures](https://www.slipseer.com/index.php?resources/makkon-textures.28/) by Makkon

skybox:

- [CS:GO Jungle Skybox for CS:S](https://gamebanana.com/mods/7251)
- converted to TGA using VIDE and IrfanView

music:

- from Jak and Daxter, from the website [Jak and Daxter Archive](https://jakanddaxterarchive.home.blog/2019/06/28/jak-and-daxter-the-precursor-legacy-official-soundtrack/).
- Its the music that plays in the Precursor Temple in Forbidden Jungle.
- hastily looped using Audacity

# notes

- [here's an AHK script](https://gist.github.com/spacehare/0f75c2348ec353a141e6d5b33fcad6fd) i use to help with wrist pain. you can toggle instead of holding down to charge the hammer
- the exit portal's layered parallax effect doesn't work in ironwail but i can't figure out why so...

"DON'T WORRY — BE FURRY"
