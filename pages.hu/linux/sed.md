# sed

> Szöveg szerkesztése szkriptelhető módon Lásd még: `awk`, `ed`. További információ: [https://www.gnu.org/software/sed/manual/sed.html.](https://www.gnu.org/software/sed/manual/sed.html)

- A `apple` (basic regex) minden előfordulását helyettesítse `mango` (basic regex) szóval az összes bemeneti sorban, és az eredményt írja ki a `stdout` címre:

`{{command}} | sed 's/apple/mango/g'`

- Egy adott szkript \[f\]ile végrehajtása és az eredmény kiírása a `stdout` címre:

`{{command}} | sed -f {{path/to/script.sed}}`

- A `apple` (extended regex) összes előfordulását helyettesítse a `APPLE` (extended regex) kifejezéssel az összes bemeneti sorban, és az eredményt írja ki a `stdout` címre:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- Csak az első sor nyomtatása a `stdout` címre:

`{{command}} | sed -n '1p'`

- A `apple` (alap regex) összes előfordulását helyettesítse a `mango` (alap regex) kifejezéssel az összes bemeneti sorban, és mentse a módosításokat egy adott fájlba:

`sed -i 's/apple/mango/g' {{path/to/file}}`
