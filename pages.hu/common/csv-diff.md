# csv-diff

> Két CSV, TSV vagy JSON fájl közötti különbségek megtekintése. További információ: <https://github.com/simonw/csv-diff>.

- Ember által olvasható összefoglaló megjelenítése a fájlok közötti különbségekről egy adott oszlop egyedi azonosítóként történő felhasználásával:

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key={{column_name}}`

- Ember által olvasható összefoglaló megjelenítése a fájlok közötti különbségekről, amely tartalmazza a legalább egy változással rendelkező sorok változatlan értékeit:

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key={{column_name}} --show-unchanged`

- A fájlok közötti különbségek összefoglalójának megjelenítése JSON formátumban egy adott oszlopot egyedi azonosítóként használva:

`csv-diff {{path/to/file1.csv}} {{path/to/file2.csv}} --key={{column_name}} --json`
