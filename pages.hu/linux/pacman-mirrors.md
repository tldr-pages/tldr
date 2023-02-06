# pacman-mirrors

> A pacman tükörlista generálása a Manjaro Linuxhoz. A pacman-mirrors minden futtatásakor szinkronizálni kell az adatbázist és frissíteni a rendszert a `sudo pacman -Syyu` segítségével. További információ: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Generáljon tükörlistát az alapértelmezett beállításokkal:

`sudo pacman-mirrors --fasttrack`

- Az aktuális tükrök állapotának lekérdezése:

`pacman-mirrors --status`

- Az aktuális ág megjelenítése:

`pacman-mirrors --get-branch`

- Váltás egy másik ágra:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Tükörlista generálása, csak az Ön országában található tükrök felhasználásával:

`sudo pacman-mirrors --geoip`
