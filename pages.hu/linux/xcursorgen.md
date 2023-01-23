# xcursorgen

> X kurzorfájl létrehozása PNG-k gyűjteményéből. A `--prefix` elhagyása esetén a képfájloknak az aktuális munkakönyvtárban kell lenniük. További információ: <https://manned.org/xcursorgen>.

- X kurzorfájl létrehozása egy konfigurációs fájl segítségével:

`xcursorgen {{path/to/config.cursor}} {{path/to/output_file}}`

- X kurzorfájl létrehozása konfigurációs fájl segítségével, és a képfájlok elérési útvonalának megadása:

`xcursorgen --prefix {{path/to/image_directory/}} {{path/to/config.cursor}} {{path/to/output_file}}`

- X kurzorfájl létrehozása konfigurációs fájl segítségével, és a kimenet írása a `stdout` címre:

`xcursorgen {{path/to/config.cursor}}`
