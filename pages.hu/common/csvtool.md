# csvtool

> Segédprogram CSV formátumú forrásokból történő adatszűrésre és -kivonásra. További információ: <https://github.com/maroofi/csvtool>.

- A második oszlop kivonása egy CSV-fájlból:

`csvtool --column {{2}} {{path/to/file.csv}}`

- A második és negyedik oszlop kivonása egy CSV-fájlból:

`csvtool --column {{2,4}} {{path/to/file.csv}}`

- Kivonja azokat a sorokat egy CSV-fájlból, ahol a második oszlop pontosan megegyezik a 'Foo'-val:

`csvtool --column {{2}} --search '{{^Foo$}}' {{path/to/file.csv}}`

- Sorok kivonása olyan CSV-fájlból, ahol a második oszlop 'Bar'-val kezdődik:

`csvtool --column {{2}} --search '{{^Bar}}' {{path/to/file.csv}}`

- Sorok keresése egy CSV-fájlban, ahol a második oszlop 'Baz'-ra végződik, majd a harmadik és hatodik oszlopok kivonása:

`csvtool --column {{2}} --search '{{Baz$}}' {{path/to/file.csv}} | csvtool --no-header --column {{3,6}}`
