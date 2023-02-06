# libreoffice

> CLI a nagy teljesítményű és ingyenes irodai programcsomaghoz, a LibreOffice-hoz. További információ: <https://www.libreoffice.org/>.

- Fájlok szóközzel elválasztott listájának megnyitása csak olvasási módban:

`libreoffice --view {{path/to/file1}} {{path/to/file2}}`

- Meghatározott fájlok tartalmának megjelenítése:

`libreoffice --cat {{path/to/file1}} {{path/to/file2}}`

- Fájlok nyomtatása egy adott nyomtatóra:

`libreoffice --pt {{printer_name}} {{path/to/file1}} {{path/to/file2}}`

- Az aktuális könyvtárban található összes `.doc` fájl átalakítása PDF-be:

`libreoffice --convert-to {{pdf}} {{*.doc}}`
