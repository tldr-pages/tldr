# mkswap

> Linux swap terület beállítása egy eszközön vagy egy fájlban. További információ: <https://manned.org/mkswap>.

- Egy adott partíció swap területként való beállítása:

`sudo mkswap {{/dev/sdb7}}`

- Egy adott fájl használata swap területként:

`sudo mkswap {{path/to/file}}`

- Egy partíció ellenőrzése a swap terület létrehozása előtt a rossz blokkok szempontjából:

`sudo mkswap -c {{/dev/sdb7}}`

- Megad egy címkét a fájlhoz (hogy a `swapon` használhassa a címkét):

`sudo mkswap -L {{swap1}} {{path/to/file}}`
