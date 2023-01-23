# doskey

> Makrók, Windows-parancsok és parancssorok kezelése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- Elérhető makrók listája:

`doskey /macros`

- Új makró létrehozása:

`doskey {{name}} = "{{command}}"`

- Új makró létrehozása egy adott futtatható programhoz:

`doskey /exename={{executable}} {{name}} = "{{command}}"`

- Makró eltávolítása:

`doskey {{name}} =`

- A memóriában tárolt összes parancs megjelenítése:

`doskey /history`

- Makrók mentése fájlba a hordozhatóság érdekében:

`doskey /macros > {{macinit}}`

- Makrók betöltése fájlból:

`doskey /macrofile = {{macinit}}`
