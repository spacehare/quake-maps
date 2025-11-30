# makkon

update

- [x] concrete
- [x] gothic stone
- [x] industrial
- [x] medieval
- [x] nature
- [x] stone
- [x] tech
- [x] urban
- [x] urban interior

# graybox layout

- [x] big picture
- [x] intro
  - [x] qbj1-esque spawn hallway
  - [x] wrench fight in the church
  - [x] wrench fight with a quad (qbj1 shotgun pillar)
  - [x] quasi-puzzle with the pistol
- [x] lake/pit
- [x] graveyard
- [x] shambler pit (that reminds me of Halo for some reason)
- [x] ravine into dungeon
- [x] DURF/OSR-esque dungeon (more free-form? rooms are puzzles? secret doors?)
  - [x] cistern
  - [x] oubliettes
  - [x] uneven terrain
  - [x] sploder ambush/jumpscare
  - [x] secret doors
- [x] qbj2 kitbash + more open "Junk Head"-esque area
- pre-staircase
  - stickflip zone
    - [x] 12 ledges, 12 ogres
    - [x] amalgam ambush
  - [-] half-donuts; to platform over their gaps ("prototype qbj2-inspired 'half-donuts'")
- [x] outro overworld
- [x] changelevel temple thing

# other

- [x] kill `_TRIGGER_ITEMS` after first weapon is acquired
- [x] use some power-ups!
- [x] Maria Scanu's Madonna
- [x] [Donald Judd block](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Donald_Judd_Concrete_Blocks.jpg/1920px-Donald_Judd_Concrete_Blocks.jpg)
- [x] trickle in swarmers more, rather than having them go in... swarms. in the Judd block area
- [x] make the wrench-only berserk fight have enemies come in waves
- [x] dog monsterjump into void
- [x] @makkon_ladder key
- [x] amalgam through concrete bars
- [x] pick a skybox
- cistern:
  > [5:31 PM]Makkon: you could make the upper part of the room brighter so you can see their silhouettes when they jump
- [-] give player opportunity to bait fiends into pits
- [-] tabernacle secret? spawn an item in it? hm
- [x] use backpacks!
- [?] change ladder colors
- [?] fix ladders (AlexUnder)
- [x] buzzing loop near lights
- [-] confessional

## feedback + observations

- [x] add Avix to playtester credit
- [x] lower the pews
- [x] make picking up vamp open a progress door
- [x] rm msg from pillar btns
- [x] fix ladder tex after 4-button pillar
- [x] make shooting the 1st bridge wizard trigger the others w ALT
- [x] slab stair window (after graveyard) -> more walkable
- [x] add bevel to pit ladder (45 deg)
- [x] railing to osr gate, where vore was
- [x] secret to 2 backpacks in OSR (post blue key)
- osr U
  - [x] shards on spinners
  - [x] drop-tower btn needs to sync w door
  - [x] change button platform sfx
- [x] +hp in lower jh intro maze
- [x] check under-trim on 3/4 jh stairs
- [x] on sk 2, amalgam vis thru ladder in h3vr room
- [x] post-h3vr ladder-dropdown needs back-tex
- [x] dog stuck on stairs @ qbj2 V
  - dog bbox too big for angles. replaced with swarmers.
- [x] +hp in invoker arena
- [x] raise final arena floor (fiends get stuck)
- [x] sk 2 ass shamblers don't trigger each other
- [x] +hp at bottom of sk2 spiral stairs
- [x] rm top vore @ spiral ?
- [x] able to bhop over outdoor secret fight for 5 invoker ammo
- [x] more monsters in cistern
- [x] when invoker is prompted -> more enemies, tougher enemies
  - [x] post-qbj2 arena
  - [x] 4 vores lined up
  - [x] 12 ogres
- [x] cut some fodder fiends (not memorable or interesting)
- [-] more platforming
- [-] make smaller/cramped rooms (contrast large and small)
- [?] harder on skill 2

## self-playtest 2025-11-19

- [x] cluster ammo around vamp in OSR 1st room
- [x] lock player in room? drop? in OSR 1st room
- [x] delay amalgam spawn more after early invoker esecret
  - [?] more amalgams?
- [x] fake dog 2nd door \_dirt
- [x] oubliette array dogs on easy only?
- [x] 7 drop shotgunners should be pistolers
- [x] osr gold key door entrance needs symmetry
- [x] holes in the wall, for jump buttons
- [x] shambler-fiend pair before gold key should be a squad
- [?] ladder to gold key needs `@makkon_ladder`
- [?] `@makkon_ladder` to post-ass bridge
- [x] 2nd HK on jh bridge move rt
- [x] slit on both sides of Mary statue
- [x] raise stairs? at jh side area after 12 dogs (can get stuck under slope)
- [x] rm glass floor under qbj1 pillar
- [x] upper jh more claustro
- [x] lower jh shrink ceil
- [x] qbj2 balcony -> qbj1 grunt couple
- [x] qbj2 V swarmers to squad
- [x] qbj2 upper B shotgunners into pistolers
- [x] qbj2 after B needs white trim on middle-step
- [x] swap '3 walls' shambler for sth else
- [x] 3 walls room could be a lil tighter
- [x] ass shambler rt shotgunner -> pistol
- [x] ass shambler more platforming in that room
- [x] rm wiz from spiral
- [x] secret fight fiends can telefrag each other
- [x] fix pillar room molding/moat
- [?] swap swarmers in invoker arena for something else, or change the arena design
- [~] too much shotgun ammo before OSR blue key

## jello 2015-11-20

- [x] why are the hot tub guys shooting each other when you shoot one...
  - alt target pattern `monster_army*` infighting bug/behavior
- [x] fish cant swim under bridge
- [x] trap player in osr 1st room
- [~] "sections that are just a big room, with enemies to the sides, are less interesting"

## self 2025-11-29

- [x] jacuzzi men trigger too early
- [x] lower guys need stairs post-jacuzzi
- [x] door in hallway post-pit should be closed if you're platforming for the secret
- [x] missing tex in post-hallway room
- [-] pre-ravine pressure, so the player can't camp at the fence in front of the building
- [x] fish visible under 3-bridges
- [x] missing tex under cistern ladder
- [x] replace OSR door triskelion decal
- [x] 2 vores in JH should aggro reinforcements as an Alt-Target
- [x] wizard on floating stairs facing bad angle
- [x] secret after doors/scissor-stairs bridge height fix
- [x] 12 buttons -> target_secret + loot (cell?)
- [x] tuck zombie into corner after spiral hallway (post-courtyard, pre-squagoda)
- [x] secret fight: make the last spike taller in the secret fight (it looks conspicuous when it's actually just arbitrary)
- [?] secret fight: return trip monsters gib each other
- [x] water should move SLOWER in genesis
- [x] shards in bad positions in genesis
- [ ] fake-dog door lighting is black. but i want dirt because it's a fake-out!
  - minlight?
- [ ] more secrets!
  - [ ] in general
  - [?] to qbj2 areas, V, B, etc
- [?] rm or delay spawn of enforcers in cool-doors room.
- [?] player can hide in monster closets in the invoker arena. this makes the fight baby-mode
- [?] mmml missable apparently
- [?] pit swarmers trigger Really early
- [?] door before vore pit? pistoler aggros too early
- [?] too many health kits after hallway??

## merge wadcleaver

`makkon_8_ind_lights`

- `makkon_industrial_grn`
- `makkon_industrial_wht`
- `makkon_industrial_brn`
- `makkon_industrial_pnk`
- `makkon_industrial_fbb`
- `makkon_industrial_fbo`
- `makkon_industrial_fbr`
- `makkon_industrial_fby`

# art stuff

- crosses
  - https://en.wikipedia.org/wiki/Christian_cross_variants
  - [x] [Cross of Lorraine](https://en.wikipedia.org/wiki/Cross_of_Lorraine)
  - [x] [Cross of Saint Peter](https://en.wikipedia.org/wiki/Cross_of_Saint_Peter)
  - [x] [Tau Cross / Saint Anthony's Cross](https://en.wikipedia.org/wiki/Tau_cross)
  - [x] [Forked Cross](https://en.wikipedia.org/wiki/Forked_cross)
  - [x] [Latin Cross](https://en.wikipedia.org/wiki/Latin_cross)

# playtest notes

playtime is about 35-45 minutes? not including deaths. estimate 40.

# weird fucking bugs

- fgd hitbox is incorrectly small
  - SOME armor shards w/o targetnames not spawning
  - armor shards w targetnames not spawning when triggered
- MML jumping becomes impossible for some reason at the end of 2 playtests so far

# priority list

1. [x] big-picture texturing. blocky brushes. (can be granular later)
1. [ ] lighting
1. [ ] subversion
1. [ ] [art pass]
1. [ ] music
1. [ ] sfx
1. [ ] granular detailing
1. [ ] phong, phong_groups
1. [ ] [main](#main)
1. [ ] angles on ladders

# main

- [x] graybox
- [x] changelevel is set to start
- [x] seal
  - [ ] optimize inside-vis
- [x] info_intermission, 1 or more
- playtest and balance
  - [x] IronWail
  - [ ] 0 easy
  - [x] 1 normal
  - [ ] 2 hard
- [x] autosaves / checkpoints; len = 25
  - [-] if co-op... also move the spawn-points ahead! (CO-OP CUT FOR SCOPE)
- coop
  - [x] test the church podium `target_secret` = yes both players get the secret
- [ ] 40 secrets
- [ ] no MAP issues in TrenchBroom console
- [ ] readme
- [ ] debug_mode for rabbitquake, so i no longer have to do this: "- [ ] replace all proto textures"

## art pass

```
"I:\Quake\tools\qpakman-062b\qpakman.exe" I:\qbj3_data\tex\* -o I:\qbj3_data\wad\qbj3_decals.wad
```

ideas

- maximalism, patterns

todo

- [x] triskelions (old symbol. apparently, eventually in medieval ages, xtians related it to holy trinity.)
- subversion
  - [ ] 'worship of other idols' narrative
  - [ ] graffiti/defacing of main structures
- [ ] amniotic fluid; raphe
- [ ] windows
- [ ] hostile architecture (urine deflectors, sitting/sleeping spikes/deterrents)
  - https://en.wikipedia.org/wiki/Hostile_architecture
  - https://en.wikipedia.org/wiki/Urine_deflector
- [ ] fog
  - [x] fog on info_player_start
- [ ] phongs, phong_groups
- [ ] unhinged scrawls on rooftops etc
- [ ] make doors prettier. add recesses for -lips etc
- [ ] more crosses to graveyard

color theory

- surface very gray and drab?
- underground more colorful and lively?
