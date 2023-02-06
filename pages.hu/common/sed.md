# sed

> Szöveg szerkesztése szkriptelhető módon Lásd még: `awk`, `ed`. További információ: [https://www.gnu.org/software/sed/manual/sed.html.](https://www.gnu.org/software/sed/manual/sed.html)

- A `apple` (basic regex) összes előfordulását helyettesítse `mango` (basic regex) szóval az összes bemeneti sorban, és az eredményt írja ki a `stdout` címre:

`{{command}} | sed 's/apple/mango/g'`

- Egy adott szkript \[f\]ile végrehajtása és az eredmény kiírása a `stdout` címre:

`{{command}} | sed -f {{path/to/script.sed}}`

- Csak az első sor nyomtatása a `stdout` címre:

`{{command}} | sed -n '1p'`
