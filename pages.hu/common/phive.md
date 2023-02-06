# phive

> A Phar telepítési és ellenőrzési környezet a PHP-alkalmazások biztonságos telepítéséhez. További információ: <https://phar.io>.

- Az elérhető alias Phar-ok listájának megjelenítése:

`phive list`

- Egy megadott Phar telepítése a helyi könyvtárba:

`phive install {{alias|url}}`

- Egy megadott Phar telepítése globálisan:

`phive install {{alias|url}} --global`

- Egy megadott Phar telepítése egy célkönyvtárba:

`phive install {{alias|url}} --target {{path/to/directory}}`

- Az összes Phar fájl frissítése a legújabb verzióra:

`phive update`

- Megadott Phar fájl eltávolítása:

`phive remove {{alias|url}}`

- A nem használt Phar fájlok eltávolítása:

`phive purge`

- Az összes elérhető parancs listázása:

`phive help`
