# getconf

> Konfigurációs értékek lekérése a Linux rendszerből. További információ: <https://manned.org/getconf.1>.

- A rendelkezésre álló konfigurációs értékek listája:

`getconf -a`

- Egy adott könyvtár konfigurációs értékeinek listázása:

`getconf -a {{path/to/directory}}`

- Ellenőrizze, hogy a linux rendszere 32 bites vagy 64 bites:

`getconf LONG_BIT`

- Ellenőrizze, hogy az aktuális felhasználó hány folyamatot futtathat egyszerre:

`getconf CHILD_MAX`

- Listázzon ki minden konfigurációs értéket, majd keressen mintákat a grep paranccsal (azaz minden olyan értéket, amelyben MAX szerepel):

`getconf -a | grep MAX`
