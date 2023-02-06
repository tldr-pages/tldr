# meld

> Grafikus diffing és merging eszköz. További információ: <https://meldmerge.org/>.

- Összevonás indítása:

`meld`

- 2 fájl összehasonlítása:

`meld {{path/to/file_1}} {{path/to/file_2}}`

- 2 könyvtár összehasonlítása:

`meld {{path/to/directory_1}} {{path/to/directory_2}}`

- 3 fájl összehasonlítása:

`meld {{path/to/file_1}} {{path/to/file_2}} {{path/to/file_3}}`

- Összehasonlítás megnyitása új lapként egy már meglévő meld példányban:

`meld --newtab {{path/to/file_1}} {{path/to/file_2}}`

- Több fájlkészlet összehasonlítása:

`meld --diff {{path/to/file_1}} {{path/to/file_2}} --diff {{path/to/file_3}} {{path/to/file_4}}`
