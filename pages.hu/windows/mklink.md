# mklink

> Szimbolikus hivatkozások létrehozása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- Szimbolikus hivatkozás létrehozása egy fájlhoz:

`mklink {{path/to/link}} {{path/to/source_file}}`

- Szimbolikus hivatkozás létrehozása egy könyvtárhoz:

`mklink /d {{path/to/link}} {{path/to/source_directory}}`

- Kemény hivatkozás létrehozása egy fájlhoz:

`mklink /h {{path/to/link}} {{path/to/source_file}}`

- Könyvtárkapcsolat létrehozása:

`mklink /j {{path/to/link}} {{path/to/source_file}}`
