# ctags

> Számos népszerű programozási nyelv forrásfájljaiban található nyelvi objektumok index (vagy tag) fájlját generálja. További információ: <https://ctags.io/>.

- Címkéket generál egyetlen fájlhoz, és azokat az aktuális könyvtárban lévő "tags" nevű fájlba adja ki, felülírva a fájlt, ha létezik:

`ctags {{path/to/file}}`

- Címkék generálása az aktuális könyvtárban lévő összes fájlhoz, és kimenetük egy adott fájlba, felülírva a fájlt, ha az létezik:

`ctags -f {{path/to/file}} *`

- Címkék generálása az aktuális könyvtárban és az összes alkönyvtárban található összes fájlhoz:

`ctags --recurse`

- Címkék generálása egyetlen fájlhoz, és kimenetük JSON formátumban, a kezdő és a záró sorszámmal együtt:

`ctags --fields=+ne --output-format=json {{path/to/file}}`
