# phpstan

> PHP statikus elemző eszköz a kódban található hibák felfedezésére. További információ: <https://github.com/phpstan/phpstan>.

- Az elemzéshez rendelkezésre álló lehetőségek megjelenítése:

`phpstan analyse --help`

- A megadott, szóközzel elválasztott könyvtárak elemzése:

`phpstan analyse {{path/to/directory}}`

- Egy könyvtár elemzése egy konfigurációs fájl segítségével:

`phpstan analyse {{path/to/directory}} --configuration {{path/to/config}}`

- Elemzés egy adott szabályszint (0-7, a magasabb szigorúbb) használatával:

`phpstan analyse {{path/to/directory}} --level {{level}}`

- Az elemzés előtt betöltendő automatikus betöltési fájl megadása:

`phpstan analyse {{path/to/directory}} --autoload-file {{path/to/autoload_file}}`

- Memóriakorlát megadása az elemzés során:

`phpstan analyse {{path/to/directory}} --memory-limit {{memory_limit}}`
