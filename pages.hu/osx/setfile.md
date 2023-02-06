# setfile

> A HFS+ könyvtárban lévő fájlok fájlattribútumainak beállítása. További információ: <https://ss64.com/osx/setfile.html>.

- Bizonyos fájlok létrehozási dátumának beállítása:

`setfile -d "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- Módosítási dátum beállítása meghatározott fájlok számára:

`setfile -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- Módosítási dátum beállítása szimlinkfájlhoz (nem magához a linkelt fájlhoz):

`setfile -P -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`
