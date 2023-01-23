# pacman

> Arch Linux csomagkezelő segédprogram. Néhány alparancsnak, mint például a `pacman sync`, saját használati dokumentációja van. Más csomagkezelőkben használt, ezzel egyenértékű parancsokért lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://man.archlinux.org/man/pacman.8>.

- Az összes csomag szinkronizálása és frissítése:

`sudo pacman -Syu`

- Új csomag telepítése:

`sudo pacman -S {{package_name}}`

- Egy csomag és függőségeinek eltávolítása:

`sudo pacman -Rs {{package_name}}`

- Keresés a csomagadatbázisban egy szabályos kifejezés vagy kulcsszó alapján:

`pacman -Ss "{{search_pattern}}"`

- Telepített csomagok és verziók listázása:

`pacman -Q`

- Csak a kifejezetten telepített csomagok és verziók listázása:

`pacman -Qe`

- Árva csomagok listázása (függőségként telepített, de valójában egyetlen csomaghoz sem szükséges):

`pacman -Qtdq`

- A teljes pacman gyorsítótár kiürítése:

`sudo pacman -Scc`
