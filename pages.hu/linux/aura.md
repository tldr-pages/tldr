# aura

> Az Aura csomagkezelő: További információ: <https://github.com/fosskers/aura>.

- Csomagok keresése a hivatalos tárolókban és az AUR-ban:

`aura --aursync --both --search {{package_name|search_regex}}`

- Csomag telepítése az AUR-ból:

`aura --aursync {{package_name}}`

- Az összes AUR csomag frissítése verbózus módban és az összes make függőség eltávolítása:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Telepítsen egy csomagot a hivatalos tárolókból:

`aura --sync {{package_name}}`

- Az összes csomag szinkronizálása és frissítése a hivatalos tárolókból:

`aura --sync --refresh --sysupgrade`

- Csomagok visszaváltása a csomagok gyorsítótárának használatával:

`aura --downgrade {{package_name}}`

- Egy csomag és függőségeinek eltávolítása:

`aura --remove --recursive --unneeded {{package_name}}`

- Árva csomagok eltávolítása (függőségként telepített, de egyetlen csomag által sem igényelt csomagok):

`aura --orphans --abandon`
