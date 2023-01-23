# vgrep

> Egy felhasználóbarát lapozó a grep-hez. Lásd még: `ugrep` `rg` További információ: <https://github.com/vrothberg/vgrep>.

- Rekurzív keresés az aktuális könyvtárban egy minta után és annak gyorsítótárba helyezése:

`vgrep {{search_pattern}}`

- A gyorsítótár tartalmának megjelenítése:

`vgrep`

- A gyorsítótárból a "4." találat megnyitása az alapértelmezett szerkesztőprogramban:

`vgrep --show {{4}}`

- A gyorsítótárban lévő minden egyes találathoz "3" soros kontextus megjelenítése:

`vgrep --show=context{{3}}`

- A találatok számának megjelenítése a fa minden egyes könyvtárában:

`vgrep --show=tree`

- A fa egyes fájljaira vonatkozó találatok számának megjelenítése:

`vgrep --show=files`

- Interaktív héj indítása a gyorsítótárban lévő találatokkal:

`vgrep --interactive`
