# pacman --sync

> Arch Linux csomagkezelő segédprogram. További információ: <https://man.archlinux.org/man/pacman.8>.

- Új csomag telepítése:

`sudo pacman --sync {{package_name}}`

- Az összes csomag szinkronizálása és frissítése (a `--downloadonly` hozzáadása a csomagok letöltéséhez és nem frissítéséhez):

`sudo pacman --sync --refresh --sysupgrade`

- Az összes csomag frissítése és egy új csomag telepítése kérés nélkül:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{package_name}}`

- Keresés a csomagadatbázisban egy reguláris kifejezés vagy kulcsszó alapján:

`pacman --sync --search "{{search_pattern}}"`

- Információk megjelenítése egy csomagról:

`pacman --sync --info {{package_name}}`

- Ellentétes fájlok felülírása csomagfrissítés során:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- Az összes csomag szinkronizálása és frissítése, de egy adott csomag figyelmen kívül hagyása (többször is használható):

`sudo pacman --sync --refresh --sysupgrade --ignore {{package_name}}`

- A nem telepített csomagok és a nem használt tárolók eltávolítása a gyorsítótárból (két `--clean` zászló használatával az összes csomag kitakarítása):

`sudo pacman --sync --clean`
