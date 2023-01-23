# rubocop

> Lint Ruby fájlok. További információ: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Az aktuális könyvtárban lévő összes fájl ellenőrzése (beleértve az alkönyvtárakat is):

`rubocop`

- Egy vagy több konkrét fájl vagy könyvtár ellenőrzése:

`rubocop {{path/to/file}} {{path/to/directory}}`

- Kimenet írása fájlba:

`rubocop --out {{path/to/file}}`

- A zsaruk (linter szabályok) listájának megtekintése:

`rubocop --show-cops`

- Kizár egy zsarut:

`rubocop --except {{cop_1}} {{cop_2}}`

- Csak a megadott zsaruk futtatása:

`rubocop --only {{cop_1}} {{cop_2}}`

- Automatikus fájljavítás (kísérleti):

`rubocop --auto-correct`
