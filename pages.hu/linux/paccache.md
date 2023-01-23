# paccache

> A pacman cache-tisztító segédprogram. További információ: <https://manned.org/paccache>.

- A pacman gyorsítótárból a 3 legfrissebb csomagverzió kivételével az összeset eltávolítja:

`paccache -r`

- A megtartandó csomagverziók számának beállítása:

`paccache -rk {{num_versions}}`

- Száraz futtatás végrehajtása és a törlésre jelölt csomagok számának megjelenítése:

`paccache -d`

- A jelölt csomagok áthelyezése egy könyvtárba törlés helyett:

`paccache -m {{path/to/directory}}`
