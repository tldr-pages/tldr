# hlint

> Eszköz a Haskell kód javításának javaslására. További információ: <http://hackage.haskell.org/package/hlint>.

- Javaslatok megjelenítése egy adott fájlhoz:

`hlint {{path/to/file}} options`

- Az összes Haskell fájl ellenőrzése és jelentés készítése:

`hlint {{path/to/directory}} --report`

- A legtöbb javaslat automatikus alkalmazása:

`hlint {{path/to/file}} --refactor`

- További opciók megjelenítése:

`hlint {{path/to/file}} --refactor-options`

- Beállítási fájl generálása, amely figyelmen kívül hagyja az összes fennálló javaslatot:

`hlint {{path/to/file}} --default > {{.hlint.yaml}}`
