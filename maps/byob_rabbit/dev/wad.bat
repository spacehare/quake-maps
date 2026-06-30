magick ./png/bun_sc_chud.png -scale 96x144! ./png/bun_sc_chud.png
magick ./png/bun_sc_grief.png -scale 96x144! ./png/bun_sc_grief.png
magick ./png/bun_sc_flat.png -scale 96x144! ./png/bun_sc_flat.png
magick ./png/bun_cliff1b.png -crop 512x64+0+0 ./png/bun_cliff1b.png
qpakman ./png/* -o I:/quake/wads/byob/byob_rabbit.wad
@REM qpakman ./png-dev/* -o I:/quake/wads/byob/byob_rabbit_dev.wad
@REM qpakman ./png-proto/* -o I:/quake/wads/byob/byob_rabbit_proto.wad