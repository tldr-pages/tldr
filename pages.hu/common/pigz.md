# pigz

> Többszálú zlib tömörítő segédprogram. További információ: <https://github.com/madler/pigz>.

- Egy fájl tömörítése alapértelmezett beállításokkal:

`pigz {{path/to/file}}`

- Egy fájl tömörítése a legjobb tömörítési módszerrel:

`pigz -9 {{path/to/file}}`

- Egy fájl tömörítése tömörítés nélkül és 4 processzorral:

`pigz -0 -p{{4}} {{path/to/file}}`

- Könyvtár tömörítése tar használatával:

`tar cf - {{path/to/directory}} | pigz > {{path/to/file}}.tar.gz`

- Egy fájl tömörítésmentesítése:

`pigz -d {{archive.gz}}`

- Az archívum tartalmának listázása:

`pigz -l {{archive.tar.gz}}`
