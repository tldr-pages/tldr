# rar

> A RAR archiváló. Támogatja a több kötetes archívumokat, amelyek opcionálisan önkitömörítőek lehetnek. További információ: <https://manned.org/rar>.

- 1 vagy több fájl archiválása:

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Könyvtár archiválása:

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- Az archívum felosztása azonos méretű részekre (50M):

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- A kapott archívum jelszóval történő védelme:

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- A fájladatok és a fejlécek jelszóval történő titkosítása:

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Egy adott tömörítési szint használata (0-5):

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`
