# pacman --upgrade

> Arch Linux csomagkezelő segédprogram. További információ: <https://man.archlinux.org/man/pacman.8>.

- Egy vagy több csomag telepítése fájlokból:

`sudo pacman --upgrade {{path/to/package1.pkg.tar.zst}} {{path/to/package2.pkg.tar.zst}}`

- Egy csomag telepítése kérés nélkül:

`sudo pacman --upgrade --noconfirm {{path/to/package.pkg.tar.zst}}`

- Ellentétes fájlok felülírása csomagtelepítés közben:

`sudo pacman --upgrade --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- Csomag telepítése a függőségi verzióellenőrzés kihagyásával:

`sudo pacman --upgrade --nodeps {{path/to/package.pkg.tar.zst}}`

- Az érintett csomagok listázása (nem telepít egyetlen csomagot sem):

`pacman --upgrade --print {{path/to/package.pkg.tar.zst}}`

- Súgó megjelenítése:

`pacman --upgrade --help`
