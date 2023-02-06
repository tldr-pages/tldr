# glab release

> A GitLab kiadványok kezelése a parancssorból. További információk: <https://glab.readthedocs.io/en/latest/release>.

- Kiadványok listázása egy Gitlab tárolóban, 30 elemre korlátozva:

`glab release list`

- Információk megjelenítése egy adott kiadásról:

`glab release view {{tag}}`

- Új kiadás létrehozása:

`glab release create {{tag}}`

- Egy adott kiadás törlése:

`glab release delete {{tag}}`

- Eszközök letöltése egy adott kiadásból:

`glab release download {{tag}}`

- Eszközök feltöltése egy adott kiadáshoz:

`glab release upload {{tag}} {{path/to/file1}} {{path/to/file2}}`
