# gow

> Figyeli a Go fájlokat, és változások esetén újraindítja az alkalmazást. További információ: <https://github.com/mitranim/gow>.

- Az aktuális könyvtár elindítása és figyelése:

`gow run .`

- Az alkalmazás elindítása a megadott argumentumokkal:

`gow run . {{argument1 argument2 ...}}`

- Alkönyvtárak figyelése verbózus üzemmódban:

`gow -v -w={{path/to/directory1,path/to/directory2,...}} run .`

- Figyelje a megadott fájlkiterjesztéseket:

`gow -e={{go,html}} run .`

- Súgó megjelenítése:

`gow -h`
