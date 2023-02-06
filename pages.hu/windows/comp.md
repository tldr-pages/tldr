# comp

> Két fájl vagy fájlkészlet tartalmának összehasonlítása. A fájlkészletek összehasonlításához használjon helyettesítő karaktereket (\*). További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Fájlok interaktív összehasonlítása:

`comp`

- Két megadott fájl összehasonlítása:

`comp {{path/to/file_1}} {{path/to/file_2}}`

- Két fájlkészlet összehasonlítása:

`comp {{path/to/directory_1/*}} {{path/to/directory_2/*}}`

- A különbségek megjelenítése tizedes formátumban:

`comp /d {{path/to/file_1}} {{path/to/file_2}}`

- Különbségek megjelenítése ASCII formátumban:

`comp /a {{path/to/file_1}} {{path/to/file_2}}`

- A különbségek sorszámainak megjelenítése:

`comp /l {{path/to/file_1}} {{path/to/file_2}}`

- Fájlok összehasonlítása esetfüggetlenül:

`comp /c {{path/to/file_1}} {{path/to/file_2}}`

- Csak az első 5 sort hasonlítja össze az egyes fájlokban:

`comp /n={{5}} {{path/to/file_1}} {{path/to/file_2}}`
