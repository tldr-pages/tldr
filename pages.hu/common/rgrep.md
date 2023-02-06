# rgrep

> Rekurzívan keres mintákat fájlokban reguláris kifejezések segítségével. A `grep -r` egyenértékű. További információ: <https://www.gnu.org/software/grep/manual/grep.html>.

- Rekurzívan keres egy mintát az aktuális munkakönyvtárban:

`rgrep "{{search_pattern}}"`

- Rekurzív keresés egy nagy- és kisbetűket nem érzékelő mintára az aktuális munkakönyvtárban:

`rgrep --ignore-case "{{search_pattern}}"`

- Kiterjesztett reguláris kifejezésminták rekurzív keresése (támogatja a `?`, `+`, `{}`, `()` és `|`) az aktuális munkakönyvtárban:

`rgrep --extended-regexp "{{search_pattern}}"`

- Pontos karakterlánc rekurzív keresése (kikapcsolja a reguláris kifejezéseket) az aktuális munkakönyvtárban:

`rgrep --fixed-strings "{{exact_string}}"`

- Rekurzív keresés egy minta után egy megadott könyvtárban (vagy fájlban):

`rgrep "{{search_pattern}}" {{path/to/file_or_directory}}`
