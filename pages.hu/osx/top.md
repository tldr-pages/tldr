# top

> Dinamikus valós idejű információk megjelenítése a futó folyamatokról. További információ: <https://ss64.com/osx/top.html>.

- Start top, minden opció elérhető a felületen:

`top`

- Start top a folyamatok belső memóriaméret szerinti rendezése (alapértelmezett sorrend - folyamatazonosító):

`top -o mem`

- Start top a folyamatokat először CPU, majd futási idő szerint rendezve:

`top -o cpu -O time`

- Start top csak az adott felhasználó tulajdonában lévő folyamatokat jeleníti meg:

`top -user {{user_name}}`

- Súgó kérése az interaktív parancsokhoz:

`?`
