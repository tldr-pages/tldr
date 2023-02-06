# gh release

> A GitHub kiadványok kezelése a parancssorból. További információk: <https://cli.github.com/manual/gh_release>.

- Kiadványok listázása egy GitHub-tárban, 30 elemre korlátozva:

`gh release list`

- Egy adott kiadásra vonatkozó információk megjelenítése:

`gh release view {{tag}}`

- Új kiadás létrehozása:

`gh release create {{tag}}`

- Egy adott kiadás törlése:

`gh release delete {{tag}}`

- Eszközök letöltése egy adott kiadásból:

`gh release download {{tag}}`

- Eszközök feltöltése egy adott kiadáshoz:

`gh release upload {{tag}} {{path/to/file1}} {{path/to/file2}}`
