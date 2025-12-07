bsp build from 2025-06-13

- [x] check IT file playback in ironwail
  - i need to use OPUS, because the VSTs (like reverb) aren't working
- [ ] shrink sky resolution
- negative surflight for void (just copy it from the qbj3 map)

# from Obsidian

- [x] refactor combat (enemies)
- [x] refactor weapons
- [x] refactor armor
- [x] refactor ammo and health pickups
- [x] test on easy
- [x] test on normal
- [x] test all secrets
- [ ] test on hard
- [ ] fix gitignore
- [x] readme
- [x] fix lighting in secrets
- [x] black doors
- [ ] black lighting in void floor areas
- 100% kills is glitched. i get 257/250 on Skill 1. the dog that jumps off the building and dies in the void counts as several kills. I don't care enough to investigate.

# fixes

qbj1 tweaks

- [x] fix elevator in residentieal area having a skewed vertex
- [x] make fake skybox bigger
- [x] alter outro text
- [x] replace textures
  - [x] find textures from half-dead R:/
    - `rabbit_makkon_animated_edit`
    - `white_concrete/ronc_white`
    - `liquids`
  - [x] replace `w_17` with `w17`
  - [x] replace `wht` with `wht1`
  - [x] `vnt_rust` with `vnt_rst`
  - [x] `conc_c_04` with `conc_c04`
- [x] make sure secret in sideways elevator is ACTUALLY ACCESSIBLE
- [x] fix nodraws on roofs
- [x] give nailgun earlier, make the nailgun room a bonus that contains the super nailgun ??
- [x] del knights that never spawn
- [x] fix skill0 softlock in blue key room with 2 fiends
- [x] fix SKILL 0 softlock in final arena
