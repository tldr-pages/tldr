# pacman --remove

> Arch Linux csomagkezelő segédprogram. További információ: <https://man.archlinux.org/man/pacman.8>.

- Egy csomag és függőségeinek eltávolítása:

`sudo pacman --remove --recursive {{package_name}}`

- Egy csomag, valamint függőségei és konfigurációs fájljai eltávolítása:

`sudo pacman --remove --recursive --nosave {{package_name}}`

- Csomag eltávolítása kérés nélkül:

`sudo pacman --remove --noconfirm {{package_name}}`

- Árva csomagok eltávolítása (függőségként telepített, de egyetlen csomag által sem igényelt csomagok):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Egy csomag és a tőle függő összes csomag eltávolítása:

`sudo pacman --remove --cascade {{package_name}}`

- Az érintett csomagok listázása (nem távolít el egyetlen csomagot sem):

`pacman --remove --print {{package_name}}`

- Az alparancs súgójának megjelenítése:

`pacman --remove --help`
