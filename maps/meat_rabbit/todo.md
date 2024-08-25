- [x] graybox
- [x] changelevel is set to start
- [x] texture
- [x] seal
- [ ] lighting
  - doors should have some minlight and/or dirt -1
  - colors to consider:
    - colder colors in concrete area (white, blue, maybe amber tho?)
    - peach, mango, beet
- [x] secrets
- playtest and balance
  - [ ] QuakeSpasm
  - [ ] IronWail
  - other players playtested; count: 3
  - [ ] 0 easy
  - [ ] 1 normal
  - [ ] 2 hard
- [ ] info_intermission, 1 or more
- [x] autosaves / checkpoints
- [ ] phongs, phong_groups
- [ ] sfx
  - [x] chomp sfx for conc hallway mouth
  - [x] snap sfx for breaking tendon door shortcuts
  - [x] CONVERT WAVS TO MONO
  - sfx on looped pillars
- [x] music
  - RAC2 "Tabora - Mining Area"
  - RAC3 "Obani Gemini"
  - RepCom "RV Alpha"
  - -> RACSM "Ryllus Temple"
- [ ] no MAP issues in TrenchBroom console
- [ ] readme
- [ ] replace all proto textures
- [x] looped pillars should not be squares
- run through map and make sure everything that needs to be detail is func_detail or func_detail_wall
- make sure mouth works on re-entering the area from the elevator
  - mouth is broken -- instead of trigger_multiple, just block that hallway w a togglewall. i don't have time to fuck with broken rotaters
- uterus floor trim
- uterus entrance (when you turn around after entering)

---

# crunch

> meat jam: 6 days left
> 1 wed: geo/tex art pass
> 2 thurs: sfx pass wrap-up
> 3 fri: more geo/tex, or lighting
> 4 sat: lighting
> 5 sun: playtesting, polish
> 6 mon: submit -- try to be done before this...

speed up phong pass by selecting every func_detail and func_detail_wall and adding phong 1, phong_group 1
then every func_group w same as above
then every structural brush into a func_group w same above

aug 21
art pass
aug 22
sfx, art pass
aug 23
art pass
aug 24
wrap up geo and tex, seal map and then move onto lighting
aug 25
==

---

- A = CONC
  - vent creaking sfx
  - vent crashing sfx
- AS = belly, after tube
  - AS = underwater section
- AS = 3 bridges
- AS (EXCEPT FOR CELING TUBE) = after 3 bridges
- AS = remobilize rm_myopia copycat area
- AS (ESCEPT FALLOPIAN TUBE JUNCTION TO ELEVATOR AND BELLY) = uterus
- AS = teeth forest until ear
  - AS = secret underwater section
- AS = ear
- AS = 3 bosses
- AS = mini respite platforming after 3 bosses
- AS = face
  - ear pond
- AS = junction between temple and shortcuts
- S = elevator
- AS = temple
  - AS = arena

---

# TRAPS !

- don't trim everything early, wait until primary art pass and then do trims if you have extra time after SFX and lighting !
- don't make everything in the art pass a round blorbo, some zigzags or fat-folds with acute angles can be OK too

# playtester feedback and demo insights

- mopey confused by rings, should i change them?
- [x] health should respawn in final arena
- [?] lyd wants more shotty ammo before-or-during teeth forest
- [x] add way back from temple
- [x] add way back from temple arena after you win
