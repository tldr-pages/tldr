# phan

> Statikus elemző eszköz PHP-hoz. További információ: <https://github.com/phan/phan>.

- A `.phan/config.php` generálása az aktuális könyvtárban:

`phan --init`

- Generál egy Phan konfigurációs fájlt egy adott szint használatával (1 a legszigorúbb, 5 a legkevésbé szigorú):

`phan --init --init-level {{level}}`

- Az aktuális könyvtár elemzése:

`phan`

- Egy vagy több könyvtár elemzése:

`phan --directory {{path/to/directory}} --directory {{path/to/another_directory}}`

- Konfigurációs fájl megadása (alapértelmezés szerint `.phan/config.php`):

`phan --config-file {{path/to/config.php}}`

- A kimeneti mód megadása:

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- A párhuzamos folyamatok számának megadása:

`phan --processes {{number_of_processes}}`
