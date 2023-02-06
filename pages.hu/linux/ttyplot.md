# ttyplot

> Valós idejű ábrázoló segédprogram a parancssorban, a `stdin` oldalon található adatokkal. További információ: <https://github.com/tenox7/ttyplot>.

- Plotolja a `1`, `2` és `3` értékeket (`cat` megakadályozza a ttyplot kilépését):

`{ echo {{1 2 3}}; cat } | ttyplot`

- Adott cím és egység beállítása:

`{ echo {{1 2 3}}; cat } | ttyplot -t {{title}} -u {{unit}}`

- Használjon while-hurkot a véletlenszerű értékek folyamatos ábrázolásához:

`{ while {{true}}; do echo {{$RANDOM}}; sleep {{1}}; done } | ttyplot`

- A `ping` kimenetének elemzése és vizualizálása:

`ping {{8.8.8.8}} | sed -u '{{s/^.*time=//g; s/ ms//g}}' | ttyplot -t "{{ping to 8.8.8.8}}" -u {{ms}}`
