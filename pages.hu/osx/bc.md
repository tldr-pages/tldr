# bc

> Egy tetszőleges pontosságú számológép nyelv. Lásd még: `dc`. További információ: [https://manned.org/man/freebsd-13.0/bc.1.](https://manned.org/man/freebsd-13.0/bc.1)

- Interaktív munkamenet indítása:

`bc`

- Interaktív munkamenet indítása a szabványos matematikai könyvtár engedélyezésével:

`bc --mathlib`

- Kifejezés kiszámítása:

`bc --expression='{{5 / 3}}'`

- Szkript végrehajtása:

`bc {{path/to/script.bc}}`

- Kifejezés kiszámítása a megadott skálával:

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- Szinusz/koinusz/arctangens/természetes logaritmus/exponenciális függvény kiszámítása a `mathlib` segítségével:

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`
