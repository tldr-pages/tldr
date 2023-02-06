# expand

> Egy vagy több Windows Cabinet fájl tömörítésének feloldása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Egyetlen fájlból álló kabinetfájl tömörítésének feloldása a megadott könyvtárba:

`expand {{path/to/file.cab}} {{path/to/directory}}`

- A forráskabinetfájlban lévő fájlok listájának megjelenítése:

`expand {{path/to/file.cab}} {{path/to/directory}} -d`

- A kabinetfájl összes fájljának kicsomagolásának feloldása:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:*`

- Egy adott fájl tömörítésének feloldása a kabinetfájlból:

`expand {{path/to/file.cab}} {{path/to/directory}} -f:{{file}}`

- A könyvtárszerkezet figyelmen kívül hagyása a tömörítés feloldásakor, és egyetlen könyvtárba helyezés:

`expand {{path/to/file.cab}} {{path/to/directory}} -i`
