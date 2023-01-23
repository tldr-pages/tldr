# unzip

> Fájlok/könyvtárak kicsomagolása ZIP-archívumokból. Lásd még: `zip`. További információ: <https://manned.org/unzip>.

- Bizonyos archívumok összes fájljának/könyvtárának kibontása az aktuális könyvtárba:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Fájlok/könyvtárak kivonása archívumokból egy adott elérési útvonalra:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}} -d {{path/to/output}}`

- Fájlok/könyvtárak kivonása archívumokból a `stdout`:

`unzip -c {{path/to/archive1.zip path/to/archive2.zip ...}}`

- A fájl(ok) tartalmának kivonása a `stdout` címre a kivont fájlnevek mellett:

`unzip -O {{gbk}} {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Egy adott archívum tartalmának listázása kivonatolás nélkül:

`unzip -l {{path/to/archive.zip}}`

- Egy adott fájl kivonása egy archívumból:

`unzip -j {{path/to/archive.zip}} {{path/to/file_in_archive1 path/to/file_in_archive2 ...}}`
