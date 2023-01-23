# dvc add

> Módosított fájlok hozzáadása az indexhez. További információ: <https://dvc.org/doc/command-reference/add>.

- Egyetlen célfájl hozzáadása az indexhez:

`dvc add {{path/to/file}}`

- Egy célkönyvtár hozzáadása az indexhez:

`dvc add {{path/to/directory}}`

- Egy adott célkönyvtár összes fájljának rekurzív hozzáadása:

`dvc add --recursive {{path/to/directory}}`

- Célfájl hozzáadása egyéni `.dvc` fájlnévvel:

`dvc add --file {{custom_name.dvc}} {{path/to/file}}`
