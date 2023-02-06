# aurman

> Arch Linux segédprogram az Arch User Repositoryból származó csomagok összeállításához és telepítéséhez. Lásd még: `pacman`. További információ: <https://github.com/polygamma/aurman>.

- Az összes csomag szinkronizálása és frissítése:

`aurman --sync --refresh --sysupgrade`

- Az összes csomag szinkronizálása és frissítése a `PKGBUILD` fájlok változásainak megjelenítése nélkül:

`aurman --sync --refresh --sysupgrade --noedit`

- Új csomag telepítése:

`aurman --sync {{package_name}}`

- Új csomag telepítése a `PKGBUILD` fájlok változásainak megjelenítése nélkül:

`aurman --sync --noedit {{package_name}}`

- Új csomag telepítése felszólítás nélkül:

`aurman --sync --noedit --noconfirm {{package_name}}`

- Keresés a csomagadatbázisban egy kulcsszóra a hivatalos tárolókból és az AUR-ból:

`aurman --sync --search {{keyword}}`

- Egy csomag és függőségeinek eltávolítása:

`aurman --remove --recursive --nosave {{package_name}}`

- A csomagok gyorsítótárának törlése (két `--clean` jelző használatával az összes csomag törléséhez):

`aurman --sync --clean`
