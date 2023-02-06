# json5

> Parancssori eszköz JSON5 fájlok JSON-ná konvertálásához. További információ: <https://json5.org>.

- JSON5 konvertálása `stdin` JSON-ba `stdout`:

`echo {{input}} | json5`

- JSON5 fájl átalakítása JSON-nak és kimenete a `stdout`:

`json5 {{path/to/input_file.json5}}`

- Egy JSON5 fájl átalakítása a megadott JSON fájlba:

`json5 {{path/to/input_file.json5}} --out-file {{path/to/output_file.json}}`

- JSON5 fájl hitelesítése:

`json5 {{path/to/input_file.json5}} --validate`

- A behúzandó szóközök számának megadása (vagy "t" a tabulátorok esetében):

`json5 --space {{indent_amount}}`

- A rendelkezésre álló opciók megtekintése:

`json5 --help`
