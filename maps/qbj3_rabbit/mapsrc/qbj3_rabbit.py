def main(context: dict):
    print("🐇 running qbj3_rabbit.py")

    var_prefix = context["var_prefix"]
    entities = context["entities"]

    for ent in entities:
        # door
        if ent.kv["classname"] == "func_door":
            ent.kv.setdefault("_minlight", "50")
            ent.kv.setdefault("sounds", "3")
            ent.kv.setdefault("_dirt", "-1")

        # purge angles
        if (
            ent.kv["classname"].startswith("trigger")
            and not ent.kv.get(var_prefix + "use_angle") == "1"
            and ent.kv.get("angle")
            and not ent.kv["classname"].endswith("monsterjump")
        ):
            print("clearing angle on %s" % ent.kv["classname"])
            del ent.kv["angle"]

        # texture swapping
        if tex := ent.kv.get(var_prefix + "replace_texture_from"):
            for brush in ent.brushes:
                for face in brush.planes:
                    if face.texture_name == tex:
                        face.texture_name = ent.kv[var_prefix + "replace_texture_with"]
