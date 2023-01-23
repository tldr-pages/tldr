# zgrep

> Szövegminták keresése tömörített fájlokban lévő fájlokból (egyenértékű a grep -Z-vel). További információ: <https://manned.org/zgrep>.

- Szövegminták keresése tömörített fájlban (nagy- és kisbetű-érzékeny):

`zgrep {{pattern}} {{path/to/compressed/file}}`

- Minta keresése tömörített fájlban (nem érzékeli a nagy- és kisbetűket):

`zgrep -i {{pattern}} {{path/to/compressed/file}}`

- A tömörített fájlban a megfelelő mintát tartalmazó sorok számának kimenete:

`zgrep -c {{pattern}} {{path/to/compressed/file}}`

- A mintát nem tartalmazó sorok megjelenítése (A keresési funkció invertálása):

`zgrep -v {{pattern}} {{path/to/compressed/file}}`

- Tömörített fájl keresése több mintára:

`zgrep -e "{{pattern_1}}" -e "{{pattern_2}}" {{path/to/compressed/file}}`

- Bővített reguláris kifejezések használata (támogatja a `?`, `+`, `{}`, `()` és `|`):

`zgrep -E {{regular_expression}} {{path/to/file}}`

- 3 sor \[C\]ontext kiírása minden egyes találat körül, \[B\]előtt vagy \[A\]után:

`zgrep -{{C|B|A}} {{3}} {{pattern}} {{path/to/compressed/file}}`
