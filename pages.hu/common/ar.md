# ar

> Unix archívumok létrehozása, módosítása és kivonása. Általában statikus könyvtárak (`.a`) és Debian csomagok (`.deb`) esetén használatos. Lásd még: `tar`. További információ: <https://manned.org/ar>.

- E\[x\]traktálja az összes tagot egy archívumból:

`ar x {{path/to/file.a}}`

- Lis\[t\] tartalom egy adott archívumban:

`ar t {{path/to/file.ar}}`

- \[r\]eplace or add specific files to an archive:

`ar r {{path/to/file.deb}} {{path/to/debian-binary path/to/control.tar.gz path/to/data.tar.xz ...}}`

- In\[s\]ert an object file index (a `ranlib` használatával egyenértékű):

`ar s {{path/to/file.a}}`

- Archívum létrehozása meghatározott fájlokkal és a hozzá tartozó objektumfájl-indexszel:

`ar rs {{path/to/file.a}} {{path/to/file1.o path/to/file2.o ...}}`
