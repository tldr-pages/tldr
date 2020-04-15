# rar

> Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się.

- Zarchiwizuj 1 lub więcej plików:

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Zarchiwizuj katalog:

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- Podziel archiwum na części równej wielkości (50M):

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Chroń hasło wynikowego archiwum:

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Szyfruj dane pliku i nagłówki za pomocą hasła:

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Użyj określonego poziomu kompresji (0-5):

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`
