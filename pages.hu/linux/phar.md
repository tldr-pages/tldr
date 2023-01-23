# phar

> PHP-archívumok létrehozása, frissítése vagy kivonatolása (PHAR). További információ: <https://manned.org/phar>.

- Szóközzel elválasztott fájlok vagy könyvtárak hozzáadása egy Phar fájlhoz:

`phar add -f {{path/to/phar_file}} {{files_or_directories}}`

- Egy Phar fájl tartalmának megjelenítése:

`phar list -f {{path/to/phar_file}}`

- Megadott fájl vagy könyvtár törlése egy Phar fájlból:

`phar delete -f {{path/to/phar_file}} -e {{file_or_directory}}`

- A teljes használati információ és a rendelkezésre álló hashing/tömörítési algoritmusok megjelenítése:

`phar help`

- A Phar-fájlban lévő fájlok és könyvtárak tömörítése vagy tömörítetlenítése:

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- Információk lekérdezése egy Phar fájlról:

`phar info -f {{path/to/phar_file}}`

- Phar fájl aláírása egy adott hash algoritmussal:

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- Phar fájl aláírása OpenSSL magánkulccsal:

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`
