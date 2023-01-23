# gdrive

> Parancssoros eszköz a Google Drive-val való interakcióhoz. A mappa/fájl azonosító a Google Drive mappájának vagy azonosítójának URL-címéből szerezhető be. További információ: <https://github.com/gdrive-org/gdrive>.

- A megadott azonosítóval rendelkező szülőmappa helyi elérési útvonalának feltöltése:

`gdrive upload -p {{id}} {{path/to/file_or_folder}}`

- Fájl vagy könyvtár letöltése az ID alapján az aktuális könyvtárba:

`gdrive download {{id}}`

- Letöltés egy adott helyi elérési útvonalra az ID alapján:

`gdrive download --path {{path/to/folder}} {{id}}`

- Egy ID új revíziójának létrehozása egy adott fájl vagy mappa felhasználásával:

`gdrive update {{id}} {{path/to/file_or_folder}}`
