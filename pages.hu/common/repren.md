# repren

> Többmintás karakterlánc-helyettesítő és fájlátnevező eszköz. További információ: <https://github.com/jlevy/repren>.

- Végezzen egy próbakört egy PNG-ket tartalmazó könyvtár átnevezésével, szó szerinti karakterlánc-helyettesítéssel:

`repren --dry-run --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- JPEG-ek könyvtárának átnevezése szabályos kifejezéssel:

`repren --rename --dry-run --from '{{regular_expression}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- CSV-fájlokból álló könyvtár tartalmának keresése és helyettesítése:

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- Egyszerre végezzen keresés-helyettesítés és átnevezés műveletet egy mintafájl segítségével:

`repren --patterns {{path/to/patfile.ext}} --full {{*.txt}}`

- Nagy- és kisbetű-független átnevezés:

`repren --rename --insensitive --patterns {{path/to/patfile.ext}} *`
