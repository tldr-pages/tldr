# mid3v2

> Hangcímkék szerkesztése. Lásd még: `id3v2`. További információ: <https://manned.org/mid3v2.1>.

- Az összes támogatott ID3v2.3 vagy ID3v2.4 keret és jelentésük felsorolása:

`id3v2 --list-frames {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Az összes támogatott ID3v1 numerikus műfaj felsorolása:

`id3v2 --list-genres {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Az adott fájlokban található összes címke listázása:

`id3v2 --list {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Konkrét előadói, album- vagy dalinformációk beállítása:

`id3v2 {{--artist|--album|--song}}={{string}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Konkrét képinformációk beállítása:

`id3v2 --picture={{filename:description:image_type:mime_type}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Konkrét évinformációk beállítása:

`id3v2 --year={{YYYY}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Konkrét dátuminformációk beállítása:

`id3v2 --date={{YYYY-MM-DD}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`
