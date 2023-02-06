# cmp

> Két fájl bájtonkénti összehasonlítása. További információ: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Kimeneti karakter és sorszám az első különbség két fájl között:

`cmp {{path/to/file1}} {{path/to/file2}}`

- Az első különbség kimeneti információi: char, sorszám, bájtok és értékek:

`cmp --print-bytes {{path/to/file1}} {{path/to/file2}}`

- Minden különbség byte-számának és értékének kimenete:

`cmp --verbose {{path/to/file1}} {{path/to/file2}}`

- Fájlok összehasonlítása, de nem ad ki semmit, csak a kilépési állapotot adja ki:

`cmp --quiet {{path/to/file1}} {{path/to/file2}}`
