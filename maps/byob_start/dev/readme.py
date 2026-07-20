import csv
from pathlib import Path

import markdown2

licenses = {
    'CC0': 'https://creativecommons.org/publicdomain/zero/1.0/deed.en',
    'CC-BY-NC 4.0 INT': 'https://creativecommons.org/licenses/by-nc/4.0/deed.en',
    'CC-BY 4.0': 'https://creativecommons.org/licenses/by/4.0/deed.en',
}


# https://docs.python.org/3/library/csv.html
def read_csv() -> list[dict]:
    SUBMISSIONS = Path(__file__).parent.parent / 'mapsrc/BYOB - submissions.tsv'
    reader = csv.DictReader(SUBMISSIONS.read_text().splitlines(), delimiter='\t', quoting=csv.QUOTE_NONE)
    obj = [row for row in reader]
    return obj


def display_users(sheet: list[dict]) -> str:
    out = ''
    headers = [
        'person',
        'stem',
        'message',
        'WAD license',
        'track number',
        'track artist',
        'track name',
        'WAD filename pattern',
    ]
    out += f'|{"|".join(headers)}|\n'
    out += f'|{"|".join(["---"] * len(headers))}|\n'
    table_rows = []
    for row in sheet:
        if row['submission status'] == 'dropped out':
            continue
        r_stem = f'`{row["stem"]}`' if row.get('stem') else ''
        r_wad = f'`{p}`' if (p := row.get('WAD filename pattern')) else ''

        wad_license = ''
        for k, v in licenses.items():
            if row['license'] == k:
                wad_license = f'[{k}]({v})'
        if wad_license == '':
            if row['license'] == 'YES':
                wad_license = 'See below'
            else:
                wad_license = row['license']

        subdata = [
            f'{row["nickname"]}',
            r_stem,
            row['message'],
            wad_license,
            row['track'],
            row['track artist'],
            row['track name'],
            r_wad,
        ]
        table_rows.append(f'|{" | ".join(subdata)}|')
    out += '\n'.join(table_rows)
    return out


def to_list(array: list) -> str:
    out = ''
    for i in array:
        out += f'- {i}\n'
    return out


def main():
    byob_parent_folder = Path(r'I:\byob')
    out_html = byob_parent_folder / 'readme.html'
    out_md = byob_parent_folder / 'readme.md'
    parent = Path(__file__).parent
    filepath = parent / 'readme.md'
    css_file = parent / 'readme.css'
    text = filepath.read_text()
    data = read_csv()

    style = f'<style>\n{css_file.read_text()}</style>\n'
    text = text.replace('$submitters', display_users(data))

    html = markdown2.markdown(style + text, extras=['tables'])

    out_md.touch(exist_ok=True)
    out_md.write_text(text)
    out_html.touch(exist_ok=True)
    out_html.write_text(html)


if __name__ == '__main__':
    main()
