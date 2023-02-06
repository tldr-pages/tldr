# xo

> Beilleszthető, konfigurációmentes linting segédprogram JavaScripthez. További információ: <https://github.com/xojs/xo>.

- Az "src" könyvtárban lévő fájlok futtatása:

`xo`

- Fájlok adott halmazának futtatása:

`xo {{file1}}.js {{file2}}.js`

- Automatikusan kijavítja a talált lint problémákat:

`xo --fix`

- Lint a tabulátorok helyett szóközöket használ behúzásként:

`xo --space`

- Lint a "szebb" kódstílus használatával:

`xo --prettier`
