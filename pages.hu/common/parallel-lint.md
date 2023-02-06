# parallel-lint

> A PHP-fájlok szintaxisának párhuzamos ellenőrzésére szolgáló eszköz. További információ: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

- Egy adott könyvtár foltozása:

`parallel-lint {{path/to/directory}}`

- Egy könyvtár foltozása a megadott számú párhuzamos folyamat használatával:

`parallel-lint -j {{processes}} {{path/to/directory}}`

- Lint egy könyvtárat, a megadott könyvtár kivételével:

`parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}`

- Fájlok könyvtárának futtatása a kiterjesztés(ek) vesszővel elválasztott listája alapján:

`parallel-lint -e {{php,html,phpt}} {{path/to/directory}}`

- Egy könyvtár futtatása és az eredmények JSON-ként történő kiadása:

`parallel-lint --json {{path/to/directory}}`

- Egy könyvtár futtatása és a hibákat tartalmazó sorok Git Blame eredményeinek megjelenítése:

`parallel-lint --blame {{path/to/directory}}`
