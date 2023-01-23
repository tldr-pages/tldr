# tr

> Karakterek fordítása: egyes karakterek és karakterkészletek alapján történő cserék futtatása. További információ: <https://www.gnu.org/software/coreutils/tr>.

- Egy karakter összes előfordulásának kicserélése egy fájlban, és az eredmény kinyomtatása:

`tr {{find_character}} {{replace_character}} < {{path/to/file}}`

- Egy karakter összes előfordulásának helyettesítése egy másik parancs kimenetéből:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Az első készlet minden egyes karakterének leképezése a második készlet megfelelő karakterére:

`tr '{{abcd}}' '{{jkmn}}' < {{path/to/file}}`

- A megadott karakterkészlet összes előfordulásának törlése a bemenetről:

`tr -d '{{input_characters}}' < {{path/to/file}}`

- Azonos karakterek sorozatának egyetlen karakterré tömörítése:

`tr -s '{{input_characters}}' < {{path/to/file}}`

- Egy fájl tartalmának nagybetűsre fordítása:

`tr "[:lower:]" "[:upper:]" < {{path/to/file}}`

- A nem nyomtatható karakterek eltávolítása a fájlból:

`tr -cd "[:print:]" < {{path/to/file}}`
