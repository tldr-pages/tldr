# pkgfile

> Arch-alapú rendszereken a hivatalos tárolókban lévő csomagokból származó fájlok keresésére szolgáló eszköz. Lásd még: `pacman files`, amely a `pacman --files` használatát írja le. További információ: <https://man.archlinux.org/man/extra/pkgfile/pkgfile.1>.

- A pkgfile adatbázis szinkronizálása:

`sudo pkgfile --update`

- Egy adott fájlt birtokló csomag keresése:

`pkgfile {{filename}}`

- Egy csomag által biztosított összes fájl listázása:

`pkgfile --list {{package_name}}`

- Csak a `bin` vagy a `sbin` könyvtárban található csomag által biztosított fájlok listázása:

`pkgfile --list --binaries {{package_name}}`

- Egy adott fájlt birtokló csomag keresése a nagy- és kisbetűket nem érzékelő párosítással:

`pkgfile --ignorecase {{filename}}`

- Egy adott fájlt birtokló csomag keresése a `bin` vagy a `sbin` könyvtárban:

`pkgfile --binaries {{filename}}`

- Egy adott fájlt birtokló csomag keresése a csomag verziójának megjelenítésével:

`pkgfile --verbose {{filename}}`

- Olyan csomag keresése, amely egy adott fájlt birtokol egy adott tárolóban:

`pkgfile --repo {{repository_name}} {{filename}}`
