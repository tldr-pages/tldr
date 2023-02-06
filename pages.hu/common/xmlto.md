# xmlto

> XSL stíluslap alkalmazása egy XML dokumentumra. További információ: <https://pagure.io/xmlto>.

- DocBook XML dokumentum átalakítása PDF formátumba:

`xmlto {{pdf}} {{document.xml}}`

- Egy DocBook XML-dokumentum átalakítása HTML-formátumba, és az így kapott fájlok tárolása egy külön könyvtárban:

`xmlto -o {{path/to/html_files}} {{html}} {{document.xml}}`

- Egy DocBook XML dokumentum átalakítása egyetlen HTML-fájllá:

`xmlto {{html-nochunks}} {{document.xml}}`

- DocBook XML dokumentum konvertálása során használandó stílustábla megadása:

`xmlto -x {{stylesheet.xsl}} {{output_format}} {{document.xml}}`
