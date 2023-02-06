# radare2

> Visszafejtő mérnöki eszközök készlete. További információ: <https://radare.gitbooks.io/radare2book/>.

- Fájl megnyitása írási módban a fájlformátum fejlécének elemzése nélkül:

`radare2 -nw {{path/to/binary}}`

- Egy program hibakeresése:

`radare2 -d {{path/to/binary}}`

- Szkript futtatása az interaktív CLI belépése előtt:

`radare2 -i {{path/to/script.r2}} {{path/to/binary}}`

- Súgószöveg megjelenítése az interaktív CLI bármely parancsához:

`> {{radare2_command}}?`

- Héjparancs futtatása az interaktív CLI-ből:

`> !{{shell_command}}`

- Az aktuális blokk nyers bájtjainak kiírása egy fájlba:

`> pr > {{path/to/file.bin}}`
