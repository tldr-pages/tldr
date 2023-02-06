# namcap

> Ellenőrizze a bináris csomagokat és a forráskódot `PKGBUILD`s a gyakori csomagolási hibák miatt. További információ: <https://man.archlinux.org/man/namcap.1>.

- Egy adott `PKGBUILD` fájl ellenőrzése:

`namcap {{path/to/pkgbuild}}`

- Egy adott csomagfájl ellenőrzése:

`namcap {{path/to/package.pkg.tar.zst}}`

- Egy fájl ellenőrzése, extra \[i\]nformációs üzenetek nyomtatása:

`namcap -i {{path/to/file}}`
