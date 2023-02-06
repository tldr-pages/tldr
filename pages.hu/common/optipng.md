# optipng

> PNG fájl optimalizáló segédprogram. További információ: <http://optipng.sourceforge.net>.

- PNG tömörítése alapértelmezett beállításokkal:

`optipng {{path/to/file.png}}`

- A PNG tömörítése a legjobb tömörítéssel:

`optipng -o{{7}} {{path/to/file.png}}`

- PNG tömörítése a leggyorsabb tömörítéssel:

`optipng -o{{0}} {{path/to/file.png}}`

- PNG tömörítése és interlacing hozzáadása:

`optipng -i {{1}} {{path/to/file.png}}`

- PNG tömörítése és az összes metaadat (beleértve a fájl időbélyegzőjét is) megőrzése:

`optipng -preserve {{path/to/file.png}}`

- PNG tömörítése és az összes metaadat eltávolítása:

`optipng -strip all {{path/to/file.png}}`
