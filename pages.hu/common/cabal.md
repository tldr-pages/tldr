# cabal

> Parancssori interfész a Haskell csomaginfrastruktúrához (Cabal). Haskell projektek és Cabal csomagok kezelése a Hackage csomagtárból. További információ: <https://cabal.readthedocs.io/en/latest/intro.html>.

- Csomagok keresése és listázása a Hackage-ből:

`cabal list {{search_string}}`

- Információk megjelenítése egy csomagról:

`cabal info {{package_name}}`

- Egy csomag letöltése és telepítése:

`cabal install {{package_name}}`

- Új Haskell projekt létrehozása az aktuális könyvtárban:

`cabal init`

- Projekt építése az aktuális könyvtárban:

`cabal build`

- A projekt tesztjeinek futtatása az aktuális könyvtárban:

`cabal test`
