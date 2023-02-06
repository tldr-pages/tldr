# apk

> Alpine Linux csomagkezelő eszköz. További információ: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Az összes távoli tároló indexének frissítése:

`apk update`

- Új csomag telepítése:

`apk add {{package}}`

- Csomag eltávolítása:

`apk del {{package}}`

- Egy csomag javítása vagy frissítése a fő függőségek módosítása nélkül:

`apk fix {{package}}`

- Csomag keresése kulcsszavak segítségével:

`apk search {{keywords}}`

- Információk megjelenítése egy adott csomagról:

`apk info {{package}}`
