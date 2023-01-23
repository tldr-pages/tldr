# kak

> A Kakoune egy mód-alapú kódszerkesztő, amely a "többszörös kiválasztás" paradigmáját valósítja meg. Az adatokat többszörös kiválasztással lehet kijelölni és egyszerre szerkeszteni különböző helyeken; a felhasználók ugyanabba a munkamenetbe is kapcsolódhatnak a közös szerkesztéshez. További információ: <https://kakoune.org>.

- Nyisson meg egy fájlt, és lépjen normál módba, parancsok végrehajtásához:

`kak {{path/to/file}}`

- Normál módból beléphet a beszúrási módba, hogy szöveget írjon a fájlba:

`i`

- Kilépés a beszúrási módból a normál módba való visszatéréshez:

`<Escape>`

- Az aktuális fájlban a "foo" minden előfordulását "bar"-ra cseréli:

`%s{{foo}}<Enter>c{{bar}}<Escape>`

- Az összes másodlagos kijelölés megszüntetése, és csak a fő kijelölés megtartása:

`<Space>`

- Keressen számokat, és válassza ki az első kettőt:

`/\d+<Enter>N`

- Egy fájl tartalmának beszúrása:

`!cat {{path/to/file}}<Enter>`

- Az aktuális fájl mentése:

`:w<Enter>`
