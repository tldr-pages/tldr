# cloc

> A forráskód sorainak és a megjegyzéseknek a megszámlálása és különbségének kiszámítása. További információ: <https://github.com/AlDanial/cloc>.

- Egy könyvtárban lévő összes kódsor megszámlálása:

`cloc {{path/to/directory}}`

- Megszámolja az összes kódsort egy könyvtárban, a számlálás során előrehaladási sávot jelenít meg:

`cloc --progress=1 {{path/to/directory}}`

- 2 könyvtárszerkezet összehasonlítása és a köztük lévő különbségek megszámolása:

`cloc --diff {{path/to/directory/one}} {{path/to/directory/two}}`

- A VCS által figyelmen kívül hagyott fájlok, például a `.gitignore` címben megadott fájlok figyelmen kívül hagyása:

`cloc --vcs git {{path/to/directory}}`

- Egy könyvtárban lévő összes kódsor megszámlálása, az egyes nyelvek helyett az egyes fájlok eredményeinek megjelenítésével:

`cloc --by-file {{path/to/directory}}`
