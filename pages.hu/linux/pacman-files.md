# pacman --files

> Arch Linux csomagkezelő segédprogram. Lásd még: `pkgfile`. További információ: <https://man.archlinux.org/man/pacman.8>.

- Frissítse a csomagadatbázist:

`sudo pacman --files --refresh`

- Keresse meg azt a csomagot, amely egy adott fájl tulajdonosa:

`pacman --files {{filename}}`

- A csomag keresése, amely egy adott fájl tulajdonosa, egy reguláris kifejezés segítségével:

`pacman --files --regex '{{regular_expression}}'`

- Csak a csomagnevek listázása:

`pacman --files --quiet {{filename}}`

- Egy adott csomag által birtokolt fájlok listázása:

`pacman --files --list {{package_name}}`

- Csak a fájlok abszolút elérési útvonalának listázása:

`pacman --query --list --quiet {{package_name}}`

- Súgó megjelenítése:

`pacman --files --help`
