# wsl-open

> Fájl vagy URL megnyitása a Windows Subsystem for Linux rendszerben a felhasználó alapértelmezett Windows GUI alkalmazásában. További információ: <https://gitlab.com/4U6U57/wsl-open>.

- Az aktuális könyvtár megnyitása a Windows Intézőben:

`wsl-open {{.}}`

- URL-cím megnyitása a felhasználó alapértelmezett Windows-böngészőjében:

`wsl-open {{https://example.com}}`

- Egy adott fájl megnyitása a felhasználó alapértelmezett Windows alkalmazásában:

`wsl-open {{path/to/file}}`

- A `wsl-open` beállítása a héj webböngészőjeként (linkek megnyitása a `wsl-open`):

`wsl-open -w`

- Súgó megjelenítése:

`wsl-open -h`
