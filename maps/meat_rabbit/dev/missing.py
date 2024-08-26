from pathlib import Path
import re

file_path = Path(r"I:\Quake\Dev\maps\maps\meat_rabbit\meat_rabbit.map")
txt = file_path.read_text(encoding='utf-8')
r = re.compile("[^\W]+(?= \[)")

matches = r.findall(txt)

unique = sorted(set(matches))

for item in unique:
    print(item)
