# ugrep

> Ultra gyors keresőeszköz a TUI lekérdezéssel. További információ: <https://github.com/Genivia/ugrep>.

- Indítson el egy lekérdezési TUI-t az aktuális könyvtárban lévő fájlok rekurzív kereséséhez (CTRL-Z a segítségért):

`ugrep --query`

- Az aktuális könyvtárban rekurzívan kereshet olyan fájlokat, amelyek tartalmaznak egy regex keresési mintát:

`ugrep "{{search_pattern}}"`

- Keresés egy adott fájlban vagy egy adott könyvtár összes fájljában, a találatok sorszámainak megjelenítésével:

`ugrep --line-number "{{search_pattern}}" {{path/to/file_or_directory}}`

- Rekurzív keresés az aktuális könyvtár összes fájljában, és minden egyező fájl nevének kiírása:

`ugrep --files-with-matches "{{search_pattern}}"`

- Fuzzy keresés olyan fájlokban, amelyekben legfeljebb 3 extra, hiányzó vagy nem egyező karakter van a mintában:

`ugrep --fuzzy={{3}} "{{search_pattern}}"`

- Tömörített fájlok, `zip` és `tar` archívumok rekurzív keresése is:

`ugrep --decompress "{{search_pattern}}"`

- Csak olyan fájlok keresése, amelyek fájlneve megfelel egy adott glob-mintának:

`ugrep --glob="{{glob_pattern}}" "{{search_pattern}}"`

- Csak a C++ forrásfájlok keresése (a `--file-type=list` használatával az összes fájltípus listázható):

`ugrep --file-type=cpp "{{search_pattern}}"`
