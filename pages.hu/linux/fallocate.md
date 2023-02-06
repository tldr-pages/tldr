# fallocate

> Lemezterület foglalása vagy felszabadítása fájloknak. A segédprogram nullázás nélkül osztja ki a helyet. További információ: <https://manned.org/fallocate>.

- Egy 700 MB lemezterületet elfoglaló fájl lefoglalása:

`fallocate --length {{700M}} {{path/to/file}}`

- Egy már kiosztott fájl 200 MiB-tal való csökkentése:

`fallocate --collapse-range --length {{200M}} {{path/to/file}}`

- Egy fájl 100 MiB után 20 MB helyet zsugorít:

`fallocate --collapse-range --offset {{100M}} --length {{20M}} {{path/to/file}}`
