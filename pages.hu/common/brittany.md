# brittany

> Haskell forrásfájlok szépen kinyomtatása. További információ: <https://github.com/lspitzner/brittany#readme>.

- Haskell forrásfájl formázása és az eredmény kiírása a `stdout` címre:

`brittany {{path/to/file.hs}}`

- Az aktuális könyvtárban lévő összes Haskell forrásfájl helyben történő formázása:

`brittany --write-mode=inplace {{*.hs}}`

- Ellenőrizze, hogy egy Haskell forrásfájl változtatásra szorul-e, és jelezze az eredményt a program kilépési kódján keresztül:

`brittany --check-mode {{path/to/file.hs}}`

- Haskell forrásfájl formázása a megadott számú szóközökkel behúzási szintenként és sorhosszonként:

`brittany --indent {{4}} --columns {{100}} {{path/to/file.hs}}`

- Haskell forrásfájl formázása a megadott konfigurációs fájlban meghatározott stílus szerint:

`brittany --config-file {{path/to/config.yaml}} {{path/to/file.hs}}`
