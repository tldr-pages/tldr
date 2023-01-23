# paru

> AUR-segédprogram és pacman wrapper. További információ: <https://github.com/Morganamilo/paru>.

- Csomagok interaktív keresése és telepítése:

`paru {{package_name_or_search_term}}`

- Az összes csomag szinkronizálása és frissítése:

`paru`

- AUR csomagok frissítése:

`paru -Sua`

- Információk lekérdezése egy csomagról:

`paru -Si {{package_name}}`

- A `PKGBUILD` és más csomagok forrásfájljainak letöltése az AUR-ból vagy az ABS-ből:

`paru --getpkgbuild {{package_name}}`

- Egy csomag `PKGBUILD` fájljának megjelenítése:

`paru --getpkgbuild --print {{package_name}}`
