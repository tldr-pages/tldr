# pacman --database

> Az Arch Linux csomagadatbázisának kezelése. A telepített csomagok bizonyos attribútumainak módosítása. További információ: <https://man.archlinux.org/man/pacman.8>.

- Egy csomag implicit telepítettként való megjelölése:

`sudo pacman --database --asdeps {{package_name}}`

- Egy csomagot kifejezetten telepítettként jelölhet meg:

`sudo pacman --database --asexplicit {{package_name}}`

- Ellenőrizze, hogy az összes csomagfüggőség telepítve van-e:

`pacman --database --check`

- Ellenőrizze a tárolókban, hogy az összes megadott függőség elérhető-e:

`pacman --database --check --check`

- Csak hibaüzenetek megjelenítése:

`pacman --database --check --quiet`

- Súgó megjelenítése:

`pacman --database --help`
