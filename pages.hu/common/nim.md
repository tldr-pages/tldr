# nim

> A Nim fordító. Feldolgozza, lefordítja és összekapcsolja a Nim nyelv forrásfájljait. További információ: <https://nim-lang.org/docs/nimc.html>.

- Forrásfájl fordítása:

`nim compile {{path/to/file.nim}}`

- Forrásfájl fordítása és futtatása:

`nim compile -r {{path/to/file.nim}}`

- Forrásfájl fordítása engedélyezett kiadásoptimalizálással:

`nim compile -d:release {{path/to/file.nim}}`

- Kis fájlméretre optimalizált kiadási bináris állomány készítése:

`nim compile -d:release --opt:size {{path/to/file.nim}}`

- HTML dokumentáció generálása egy modulhoz (a kimenet az aktuális könyvtárba kerül):

`nim doc {{path/to/file.nim}}`

- Egy fájl szintaxis és szemantikai ellenőrzése:

`nim check {{path/to/file.nim}}`
