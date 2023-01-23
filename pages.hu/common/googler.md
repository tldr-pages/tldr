# googler

> Keresés a Google-ban parancssorból. További információ: <https://github.com/jarun/googler>.

- Keresés a Google-ban egy kulcsszóra:

`googler {{keyword}}`

- Keressen rá a Google-ra, és nyissa meg az első találatot a webböngészőben:

`googler -j {{keyword}}`

- N keresési eredmény megjelenítése (alapértelmezett 10):

`googler -n {{N}} {{keyword}}`

- Automatikus helyesírás-javítás kikapcsolása:

`googler -x {{keyword}}`

- Keresés egy oldalon egy kulcsszóra:

`googler -w {{site}} {{keyword}}`

- Google keresési eredmény megjelenítése JSON formátumban:

`googler --json {{keyword}}`

- Helyszíni önfrissítés végrehajtása:

`googler -u`

- További segítség interaktív módban:

`?`
