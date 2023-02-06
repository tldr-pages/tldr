# godoc

> A go csomagok dokumentációjának megjelenítése. További információ: <https://godoc.org/>.

- Az "fmt" csomag súgójának megjelenítése:

`godoc {{fmt}}`

- Az "fmt" csomag "Printf" függvényének súgójának megjelenítése:

`godoc {{fmt}} {{Printf}}`

- Dokumentáció kiszolgálása webkiszolgálóként a 6060-as porton:

`godoc -http=:{{6060}}`

- Indexfájl létrehozása:

`godoc -write_index -index_files={{path/to/file}}`

- A megadott indexfájl használata a dokumentációban való kereséshez:

`godoc -http=:{{6060}} -index -index_files={{path/to/file}}`
