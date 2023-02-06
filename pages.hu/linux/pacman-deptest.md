# pacman --deptest

> Ellenőrzi az egyes megadott függőségeket, és visszaadja a rendszerben jelenleg nem teljesített függőségek listáját. További információ: <https://man.archlinux.org/man/pacman.8>.

- Kiírja a nem telepített függőségek csomagneveit:

`pacman --deptest {{package_name1}} {{package_name2}}`

- Ellenőrzi, hogy a telepített csomag megfelel-e a megadott minimális verziónak:

`pacman --deptest "{{bash>=5}}"`

- Ellenőrizze, hogy egy csomag későbbi verziója telepítve van-e:

`pacman --deptest "{{bash>5}}"`

- Súgó megjelenítése:

`pacman --deptest --help`
