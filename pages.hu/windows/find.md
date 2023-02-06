# find

> Egy megadott karakterlánc keresése egy vagy több fájlban. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Meghatározott karakterláncot tartalmazó sorok keresése:

`find "{{string}}" {{path/to/file_or_directory}}`

- A megadott karakterláncot nem tartalmazó sorok megjelenítése:

`find "{{string}}" {{path/to/file_or_directory}} /v`

- A megadott karakterláncot tartalmazó sorok számának megjelenítése:

`find "{{string}}" {{path/to/file_or_directory}} /c`

- Sorszámok megjelenítése a sorok listájával együtt:

`find "{{string}}" {{path/to/file_or_directory}} /n`
