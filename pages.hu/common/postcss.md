# postcss

> A PostCSS egy eszköz a stílusok átalakítására JS pluginokkal. További információ: <https://postcss.org>.

- CSS fájl elemzése és átalakítása:

`postcss {{path/to/file}}`

- CSS-fájl elemzése és átalakítása, valamint kimenet egy adott fájlba:

`postcss {{path/to/file}} --output {{path/to/file}}`

- CSS-fájl elemzése és átalakítása és kimenet egy adott könyvtárba:

`postcss {{path/to/file}} --dir {{path/to/directory}}`

- CSS-fájl elemzése és átalakítása helyben:

`postcss {{path/to/file}} --replace`

- Egyéni PostCSS elemző megadása:

`postcss {{path/to/file}} --parser {{parser}}`

- Egyéni PostCSS szintaxis megadása:

`postcss {{path/to/file}} --syntax {{syntax}}`

- A CSS-fájl változásainak figyelése:

`postcss {{path/to/file}} --watch`

- A rendelkezésre álló opciók és példák megjelenítése:

`postcss --help`
