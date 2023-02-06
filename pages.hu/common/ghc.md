# ghc

> The Glasgow Haskell Compiler. Haskell forrásfájlok fordítása és összekapcsolása. További információ: <https://www.haskell.org/ghc>.

- Megkeresi és lefordítja az összes modult az aktuális könyvtárban:

`ghc Main`

- Egyetlen fájl fordítása:

`ghc {{file.hs}}`

- Kompilálás extra optimalizálással:

`ghc -O {{file.hs}}`

- Leállítja a fordítást az objektumfájlok (.o) generálása után:

`ghc -c {{file.hs}}`

- REPL (interaktív shell) indítása:

`ghci`

- Egyetlen kifejezés kiértékelése:

`ghc -e {{expression}}`
