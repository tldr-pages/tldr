# raco

> Racket parancssori eszközök. További információ: <https://docs.racket-lang.org/raco/>.

- Egy csomag telepítése, a függőségek automatikus telepítése:

`raco pkg install --auto {{package_source}}`

- Telepítse az aktuális könyvtárat csomagként:

`raco pkg install`

- Bájtkód, dokumentáció, futtatható fájlok és metaadat-indexek összeállítása (vagy újraépítése) a gyűjteményekhez:

`raco setup {{collection1 collection2 ...}}`

- Tesztek futtatása fájlokban:

`raco test {{path/to/tests1.rkt path/to/tests2.rkt ...}}`

- Helyi dokumentáció keresése:

`raco docs {{search_terms ...}}`

- Súgó megjelenítése:

`raco help`
