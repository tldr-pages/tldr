# siege

> HTTP terheléstesztelő és benchmarking eszköz. További információ: <https://www.joedog.org/siege-manual/>.

- Teszteljen egy URL-címet alapértelmezett beállításokkal:

`siege {{https://example.com}}`

- URL-ek listájának tesztelése:

`siege --file {{path/to/url_list.txt}}`

- URL-ek listájának tesztelése véletlenszerű sorrendben (Internetforgalom szimulálása):

`siege --internet --file {{path/to/url_list.txt}}`

- URL-ek listájának teljesítményértékelése (a kérések közötti várakozás nélkül):

`siege --benchmark --file {{path/to/url_list.txt}}`

- Egyidejű kapcsolatok számának beállítása:

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- Állítsa be, hogy az ostrom mennyi ideig tartson:

`siege --time={{30s}} --file {{path/to/url_list.txt}}`
