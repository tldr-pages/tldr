# GetFileInfo

> Információszerzés egy HFS+ könyvtárban lévő fájlról. További információ: <https://www.unix.com/man-page/osx/1/GetFileInfo/>.

- Információk megjelenítése egy adott fájlról:

`GetFileInfo {{path/to/filename}}`

- Az adott fájl létrehozásának dátumának és időpontjának megjelenítése:

`GetFileInfo -d {{path/to/filename}}`

- Az adott fájl utolsó módosításának dátuma és időpontja:

`GetFileInfo -m {{path/to/filename}}`

- Az adott fájl létrehozójának megjelenítése:

`GetFileInfo -c {{path/to/filename}}`
