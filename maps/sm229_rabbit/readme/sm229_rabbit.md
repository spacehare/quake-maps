## [map sources](https://github.com/spacehare/quake-maps)

# credit

- textures by me LOL
  - i made them all in Krita with a "Star 03 V2" XP-PEN tablet -- the `.kra`, `.wad`, `.png` files are included on github 😛
    - `_Charcoal_Pencil_Medium` my beloved

# technical

- [TrenchBroom 2024.1](https://trenchbroom.github.io/)
- [ericw-tools-2.0.0-alpha8-win64](https://github.com/ericwa/ericw-tools/releases/tag/2.0.0-alpha8)
- compile profile
  - `QBSP` `-leaktest -splitturb -bsp2 build/${MAP_BASE_NAME}.map maps/${MAP_BASE_NAME}.bsp`
  - `VIS` `-noambient -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`
  - `LIGHT` `-emissivequality high -extra4 -threads ${CPU_COUNT - 1} maps/${MAP_BASE_NAME}.bsp`

# secrets

- the messages in the secrets are the opening lyrics to the song "Can't Get Arrested" by Nik Kershaw
  - it's a song my ex liked; he recommended me a bunch of albums years ago. we don't talk very often anymore. i listened to some albums while mapping.

# DON'T WORRY — BE FURRY
