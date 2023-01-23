# takeown

> Egy fájl vagy könyvtár tulajdonjogának átvétele. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- A megadott fájl tulajdonjogának átvétele:

`takeown /f {{path/to/file}}`

- A megadott könyvtár tulajdonjogának átvétele:

`takeown /d {{path/to/directory}}`

- A megadott könyvtár és az összes alkönyvtár tulajdonjogának átvétele:

`takeown /r /d {{path/to/directory}}`

- A tulajdonjogot az aktuális felhasználó helyett a Rendszergazda csoportra változtatja:

`takeown /a /f {{path/to/file}}`
