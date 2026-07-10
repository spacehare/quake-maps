from rabbitquake.app import wad

ex = wad.WAD.from_wad_file(r'I:\byob\CHIMERA2.wad')

pairs = zip(ex.entries, ex.textures)

for e, t in pairs:
    print(e.name, t.name)
