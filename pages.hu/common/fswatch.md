# fswatch

> Platformokon átívelő fájlváltoztatási monitor. További információ: <https://emcrisostomo.github.io/fswatch>.

- Bash parancs futtatása fájl létrehozásakor, frissítésekor vagy törlésekor:

`fswatch {{path/to/file}} | xargs -n 1 {{bash_command}}`

- Egy vagy több fájl és/vagy könyvtár megfigyelése:

`fswatch {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -n 1 {{bash_command}}`

- Kiírja a megváltozott fájlok abszolút elérési útvonalait:

`fswatch {{path/to/directory}} | xargs -n 1 -I {} echo {}`

- Szűrés az esemény típusa szerint:

`fswatch --event {{Updated|Deleted|Created}} {{path/to/directory}} | xargs -n 1 {{bash_command}}`
