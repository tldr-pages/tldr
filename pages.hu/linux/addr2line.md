# addr2line

> A bináris címek átalakítása fájlnevekké és sorszámokká. További információ: <https://manned.org/addr2line>.

- A forráskód fájlnevének és sorszámának megjelenítése egy végrehajtható program utasításcíméből:

`addr2line --exe={{path/to/executable}} {{address}}`

- A funkció nevének, fájlnevének és sorszámának megjelenítése:

`addr2line --exe={{path/to/executable}} --functions {{address}}`

- C++ kód esetén a függvénynév szétválasztása:

`addr2line --exe={{path/to/executable}} --functions --demangle {{address}}`
