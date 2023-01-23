# tokei

> Egy program, amely statisztikákat nyomtat ki a kódokról. További információ: <https://github.com/XAMPPRocky/tokei>.

- Jelentés készítése egy könyvtárban és az összes alkönyvtárban található kódról:

`tokei {{path/to/directory}}`

- Egy könyvtárra vonatkozó jelentés lekérdezése a `.min.js` fájlok kivételével:

`tokei {{path/to/directory}} -e {{*.min.js}}`

- Egy könyvtárban lévő egyes fájlok statisztikáinak kinyomtatása:

`tokei {{path/to/directory}} --files`

- Rust és Markdown típusú fájlokra vonatkozó jelentés lekérdezése:

`tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}`
