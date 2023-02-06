# sed

> Szöveg szerkesztése szkriptelhető módon Lásd még: `awk`, `ed`. További információ: [https://keith.github.io/xcode-man-pages/sed.1.html.](https://keith.github.io/xcode-man-pages/sed.1.html)

- A `apple` (basic regex) minden előfordulását helyettesítse `mango` (basic regex) szóval az összes bemeneti sorban, és az eredményt írja ki a `stdout` címre:

`{{command}} | sed 's/apple/mango/g'`

- Egy adott szkript \[f\]ile végrehajtása és az eredmény kiírása a `stdout` címre:

`{{command}} | sed -f {{path/to/script.sed}}`

- A `apple` (kiterjesztett regex) összes előfordulását helyettesítse a `APPLE` (kiterjesztett regex) kifejezéssel az összes bemeneti sorban, és az eredményt írja ki a `stdout` címre:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- Csak az első sor nyomtatása a `stdout` címre:

`{{command}} | sed -n '1p'`

- Cserélje ki a `apple` (alap regex) összes előfordulását a `mango` (alap regex) szóval a `file` oldalon, és mentse el az eredeti adatot a `file.bak` címre:

`sed -i bak 's/apple/mango/g' {{path/to/file}}`
