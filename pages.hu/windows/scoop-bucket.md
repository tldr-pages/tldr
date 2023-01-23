# scoop bucket

> Vödrök kezelése: Ha a Scoop nem tudja, hol található a vödör, akkor meg kell adni a tároló helyét. További információ: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- A jelenleg használt vödrök listázása:

`scoop bucket list`

- Az összes ismert vödör listázása:

`scoop bucket known`

- Egy ismert vödör hozzáadása a neve alapján:

`scoop bucket add {{name}}`

- Ismeretlen vödör hozzáadása a neve és a Git-tárhely URL-címe alapján:

`scoop bucket add {{name}} {{https://example.com/repository.git}}`

- Egy vödör eltávolítása a neve alapján:

`scoop bucket rm {{name}}`
