# phpunit

> PHPUnit parancssori tesztfutó. További információ: <https://phpunit.de>.

- Tesztek futtatása az aktuális könyvtárban. Megjegyzés: Elvárja, hogy legyen egy 'phpunit.xml':

`phpunit`

- Tesztek futtatása egy adott fájlban:

`phpunit {{path/to/TestFile.php}}`

- A megadott csoporttal megjegyzett tesztek futtatása:

`phpunit --group {{name}}`

- Tesztek futtatása és HTML formátumú lefedettségi jelentés készítése:

`phpunit --coverage-html {{path/to/directory}}`
