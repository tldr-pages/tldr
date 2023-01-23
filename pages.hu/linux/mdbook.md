# mdbook

> Online könyvek készítése Markdown fájlok írásával. További információ: <https://rust-lang.github.io/mdBook/>.

- Hozzon létre egy mdbook projektet az aktuális könyvtárban:

`mdbook init`

- Létrehoz egy mdbook projektet egy adott könyvtárban:

`mdbook init {{path/to/directory}}`

- Tisztítsa meg a könyvtárat a létrehozott könyvvel:

`mdbook clean`

- Könyv kiszolgálása a `http://localhost:3000` címen, automatikus készítés a fájlváltozásoknál:

`mdbook serve`

- Markdown fájlok egy halmazának figyelése és automatikus építés, amikor egy fájl változik:

`mdbook watch`
