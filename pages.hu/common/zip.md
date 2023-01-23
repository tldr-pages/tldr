# zip

> Fájlok csomagolása és tömörítése (archiválása) zip-fájlba. Lásd még: `unzip`. További információ: <https://manned.org/zip>.

- Fájlok/könyvtárak hozzáadása egy adott archívumhoz (\[r\]ekurzívan):

`zip -r {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Fájlok/könyvtárak eltávolítása egy adott archívumból (\[d\]elete):

`zip -d {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Fájlok/könyvtárak archiválása e\[x\]cluding specified files/directories:

`zip -r {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} -x {{path/to/excluded_files_or_directories}}`

- Fájlok/könyvtárak archiválása meghatározott tömörítési szinttel (`0` - a legalacsonyabb, `9` - a legmagasabb):

`zip -r -{{0-9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- \[e\]titkosított archívum létrehozása egy adott jelszóval:

`zip -r -e {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Fájlok/könyvtárak archiválása többrészes \[s\]plit zip fájlba (pl. 3 GB-os részek):

`zip -r -s {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Egy adott archívum tartalmának kinyomtatása:

`zip -sf {{path/to/compressed.zip}}`
