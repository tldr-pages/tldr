# bc

> Egy tetszőleges pontosságú számológép nyelv. Lásd még: `dc`. További információ: [https://manned.org/man/bc.1.](https://manned.org/man/bc.1)

- Interaktív munkamenet indítása:

`bc`

- Interaktív munkamenet indítása a szabványos matematikai könyvtár engedélyezésével:

`bc --mathlib`

- Kifejezés kiszámítása:

`echo '{{5 / 3}}' | bc`

- Szkript végrehajtása:

`bc {{path/to/script.bc}}`

- Kifejezés kiszámítása a megadott skálával:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Szinusz/koinusz/arctangens/természetes logaritmus/exponenciális függvény kiszámítása a `mathlib` segítségével:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`
