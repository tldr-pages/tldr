# pdfgrep

> Szövegkeresés PDF-fájlokban. További információ: <https://pdfgrep.org>.

- A mintának megfelelő sorok keresése egy PDF-ben:

`pdfgrep {{pattern}} {{file.pdf}}`

- Tartalmazza a fájl nevét és az oldalszámot minden egyes egyező sorhoz:

`pdfgrep --with-filename --page-number {{pattern}} {{file.pdf}}`

- A "foo" betűvel kezdődő sorok keresése a nagy- és kisbetűket nem figyelembe véve, és az első 3 találatot adja vissza:

`pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{file.pdf}}`

- A minta keresése a `.pdf` kiterjesztésű fájlokban az aktuális könyvtárban rekurzív módon:

`pdfgrep --recursive {{pattern}}`

- Mintakeresés az aktuális könyvtárban lévő, egy adott globusnak megfelelő fájlokban rekurzívan:

`pdfgrep --recursive --include {{'*book.pdf'}} {{pattern}}`
