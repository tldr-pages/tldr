# yaa

> YAA-archívumok létrehozása és kezelése. További információ: <https://www.manpagez.com/man/1/yaa/>.

- Archívum létrehozása egy könyvtárból:

`yaa archive -d {{path/to/directory}} -o {{path/to/output.yaa}}`

- Archívum létrehozása fájlból:

`yaa archive -i {{path/to/file}} -o {{path/to/output.yaa}}`

- Archívum kicsomagolása az aktuális könyvtárba:

`yaa extract -i {{path/to/archive.yaa}}`

- Egy archívum tartalmának listázása:

`yaa list -i {{path/to/archive.yaa}}`

- Archívum létrehozása egy adott tömörítési algoritmussal:

`yaa archive -a {{algorithm}} -d {{path/to/directory}} -o {{path/to/output.yaa}}`

- Archívum létrehozása 8 MB-os blokkmérettel:

`yaa archive -b {{8m}} -d {{path/to/directory}} -o {{path/to/output.yaa}}`
