- [x] graybox
- [x] changelevel is set to start
- [x] texture
- [x] seal
- [x] lighting
  - doors should have some minlight and/or dirt -1
  - colors to consider:
    - colder colors in concrete area (white, blue, maybe amber tho?)
    - peach, mango, beet
- [x] secrets
- playtest and balance
  - [x] QuakeSpasm
  - [x] IronWail
  - other players playtested; count: 3
  - [x] 0 easy
  - [x] 1 normal
  - [x] 2 hard
- [x] info_intermission, 1 or more
- [x] autosaves / checkpoints
- [ ] phongs, phong_groups !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- [x] sfx
  - [x] chomp sfx for conc hallway mouth
  - [x] snap sfx for breaking tendon door shortcuts
  - [x] CONVERT WAVS TO MONO
  - [-] sfx on looped pillars
- [x] music
  - RAC2 "Tabora - Mining Area"
  - RAC3 "Obani Gemini"
  - RepCom "RV Alpha"
  - -> RACSM "Ryllus Temple"
- [x] no MAP issues in TrenchBroom console
- [x] readme
- [x] replace all proto textures
- [x] looped pillars should not be squares
- [x] run through map and make sure everything that needs to be detail is func_detail or func_detail_wall
- [-] make sure mouth works on re-entering the area from the elevator
  - mouth is broken -- instead of trigger_multiple, just block that hallway w a togglewall. i don't have time to fuck with broken rotaters
- [x] uterus floor trim
  - i am tired of working on this. i'm gonna have it skew into the acid and call it a day lol
- [x] uterus entrance (when you turn around after entering)
- make sure "sounds" (meant to be silent, like doors) are set to 0 and not -1, or else you get a sv precache console warning

- [x] playthrough on easy, getting all secrets
- [x] playthrough on normal with light/phong debug and check the env geo
- after zipping, run through the unzipped map to make sure all sfx are correct and stuff

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
^ ended up not actually doing this

aug 21
art pass
aug 22
sfx, art pass
aug 23
art pass
aug 24
wrap up geo and tex, seal map and then move onto lighting
aug 25
lighting, minor tex and geo
submit

---

- ASL = CONC
  - [x] vent creaking sfx
  - [x] vent crashing sfx
- ASL = belly, after tube
  - ASL = underwater section
- ASL = 3 bridges
- ASL = after 3 bridges
- ASL = remobilize rm_myopia copycat area
- ASL = uterus
- ASL = teeth forest until ear
  - ASL = secret underwater section
- ASL = ear
- ASL = 3 bosses
- ASL = mini respite platforming after 3 bosses
- ASL = face
  - ear pond
- ASL = junction between temple and shortcuts
- ASL = elevator
- ASL = temple
  - ASL = arena

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
