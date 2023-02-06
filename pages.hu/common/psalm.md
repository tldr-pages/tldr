# psalm

> Statikus elemző eszköz a PHP-alkalmazások hibáinak keresésére. További információ: <https://psalm.dev>.

- Psalm konfiguráció generálása:

`psalm --init`

- Az aktuális munkakönyvtár elemzése:

`psalm`

- Egy adott könyvtár vagy fájl elemzése:

`psalm {{path/to/file_or_directory}}`

- Egy projekt elemzése egy adott konfigurációs fájllal:

`psalm --config {{path/to/psalm.xml}}`

- Információs megállapítások felvétele a kimenetbe:

`psalm --show-info`

- Projekt elemzése és statisztikák megjelenítése:

`psalm --stats`

- Projekt elemzése párhuzamosan 4 szálon:

`psalm --threads {{4}}`
