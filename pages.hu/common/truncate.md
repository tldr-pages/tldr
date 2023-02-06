# truncate

> Egy fájl méretének a megadott méretre történő kicsinyítése vagy bővítése. További információ: <https://www.gnu.org/software/coreutils/truncate>.

- 10 GB-os méret beállítása egy meglévő fájlhoz, vagy egy új fájl létrehozása a megadott mérettel:

`truncate --size {{10G}} {{filename}}`

- A fájl méretének 50 MiB-tal való bővítése, lyukakkal való kitöltése (ami nulla bájtként olvasható):

`truncate --size +{{50M}} {{filename}}`

- Csökkentse a fájlt 2 GiB-tal, a fájl végéről adatok eltávolításával:

`truncate --size -{{2G}} {{filename}}`

- A fájl tartalmának kiürítése:

`truncate --size 0 {{filename}}`

- Ürítse ki a fájl tartalmát, de ne hozza létre a fájlt, ha az nem létezik:

`truncate --no-create --size 0 {{filename}}`
