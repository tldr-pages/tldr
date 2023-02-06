# help2man

> Egyszerű man oldalak készítése egy futtatható program `--help` és `--version` kimenetéből. További információ: <https://www.gnu.org/software/help2man>.

- Man oldal létrehozása egy futtatható programhoz:

`help2man {{executable}}`

- Adja meg a man oldal "name" bekezdését:

`help2man {{executable}} --name {{name}}`

- Adja meg a man oldal szakaszát (alapértelmezett értéke 1):

`help2man {{executable}} --section {{section}}`

- Kimenet egy fájlba a `stdout` helyett:

`help2man {{executable}} --output {{path/to/file}}`

- Részletes súgó megjelenítése:

`help2man --help`
