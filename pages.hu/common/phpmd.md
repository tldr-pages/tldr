# phpmd

> Egy PHP rendetlenségdetektor, amely ellenőrzi a leggyakoribb lehetséges problémákat. További információ: <https://github.com/phpmd/phpmd>.

- A rendelkezésre álló szabálykészletek és formátumok listájának megjelenítése:

`phpmd`

- Egy fájl vagy könyvtár átvizsgálása problémák után vesszővel elválasztott szabálykészletekkel:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}}`

- A szabályok minimális prioritási küszöbértékének megadása:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --minimumpriority {{priority}}`

- Csak a megadott kiterjesztések bevonása az elemzésbe:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --suffixes {{extensions}}`

- A megadott, vesszővel elválasztott könyvtárak kizárása:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --exclude {{directory_patterns}}`

- Az eredmények kiadása a `stdout` helyett egy fájlba:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --reportfile {{path/to/report_file}}`

- Figyelmeztetést elnyomó PHPDoc-kommentárok használatának figyelmen kívül hagyása:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --strict`
