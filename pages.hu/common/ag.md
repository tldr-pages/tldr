# ag

> Az ezüst kereső. Olyan, mint az ack, de célja, hogy gyorsabb legyen. További információ: <https://github.com/ggreer/the_silver_searcher>.

- A "foo" szót tartalmazó fájlok keresése, és a sorok találatainak kiírása kontextusban:

`ag {{foo}}`

- A "foo" szót tartalmazó fájlok keresése egy adott könyvtárban:

`ag {{foo}} {{path/to/directory}}`

- A "foo"-t tartalmazó fájlok keresése, de csak a fájlneveket listázza:

`ag -l {{foo}}`

- A "FOO"-t tartalmazó fájlok keresése esetfüggetlenül, és csak az egyezést írja ki, nem pedig az egész sort:

`ag -i -o {{FOO}}`

- A "foo" szót olyan fájlokban keresse, amelyek neve megegyezik a "bar" névvel:

`ag {{foo}} -G {{bar}}`

- Olyan fájlok keresése, amelyek tartalma megfelel egy reguláris kifejezésnek:

`ag '{{^ba(r|z)$}}'`

- Keresés olyan fájlokban, amelyek neve megegyezik a "foo"-val:

`ag -g {{foo}}`
