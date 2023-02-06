# dir

> A könyvtárak tartalmának listázása fájlonként egy sorban, a speciális karaktereket backslash escape szekvenciák jelölik. Úgy működik, mint a `ls -C --escape`. További információ: <https://manned.org/dir>.

- Az összes fájl listázása, beleértve a rejtett fájlokat is:

`dir -all`

- Fájlok listázása a szerzőjükkel együtt (`-l` szükséges):

`dir -l --author`

- Fájlok listázása, kivéve azokat, amelyek megfelelnek egy megadott blob-mintának:

`dir --hide={{pattern}}`

- Alkönyvtárak rekurzív listázása:

`dir --recursive`

- Súgó megjelenítése:

`dir --help`
