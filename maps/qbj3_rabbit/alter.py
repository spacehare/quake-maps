from pathlib import Path

from rabbitquake.app.parse import dumps, loads

AUTOSAVE_LAYER_ID = '1124538'

if __name__ == '__main__':
    level_path: Path = Path(Path(__file__) / 'mapsrc/qbj3_rabbit.map')
    output_path: Path = level_path.with_stem(level_path.stem + '_altered')

    entities = loads(level_path.read_text())

    for ent in entities:
        for key, value in ent.kv.items():
            if key.startswith('target') and value == '_AUTOSAVE':
                break
        else:
            ent.kv['_tb_layer'] = AUTOSAVE_LAYER_ID
        continue

    output_path.write_text(dumps(entities))
