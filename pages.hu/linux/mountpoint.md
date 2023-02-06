# mountpoint

> Annak tesztelése, hogy egy könyvtár egy fájlrendszer csatlakoztatási pontja-e. További információ: <https://manned.org/mountpoint>.

- Annak ellenőrzése, hogy egy könyvtár mountpoint-e:

`mountpoint {{path/to/directory}}`

- Annak ellenőrzése, hogy egy könyvtár mountpoint-e, anélkül, hogy bármilyen kimenetet megjelenítene:

`mountpoint -q {{path/to/directory}}`

- A mountpoint fájlrendszerének major/minor számainak megjelenítése:

`mountpoint --fs-devno {{path/to/directory}}`
