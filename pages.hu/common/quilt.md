# quilt

> Foltok sorozatának kezelésére szolgáló eszköz. További információ: <https://savannah.nongnu.org/projects/quilt>.

- Meglévő javítás importálása fájlból:

`quilt import {{path/to/filename.patch}}`

- Új javítás létrehozása:

`quilt new {{filename.patch}}`

- Fájl hozzáadása az aktuális javításhoz:

`quilt add {{path/to/file}}`

- A fájl szerkesztése után frissítse az aktuális javítást a módosításokkal:

`quilt refresh`

- Alkalmazza a sorozatfájlban lévő összes foltot:

`quilt push -a`

- Az összes alkalmazott folt eltávolítása:

`quilt pop -a`
