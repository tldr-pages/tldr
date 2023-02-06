# progress

> A coreutils futtatásának előrehaladásának megjelenítése/ellenőrzése. További információ: <https://github.com/Xfennec/progress>.

- A coreutils futásának előrehaladásának megjelenítése:

`progress`

- A coreutils csendes üzemmódban történő futtatásának előrehaladásának megjelenítése:

`progress -q`

- Egyetlen hosszan futó parancs elindítása és figyelése:

`{{command}} & progress --monitor --pid $!`

- A befejezésig hátralévő idő becsült értékének feltüntetése:

`progress --wait --command {{firefox}}`
