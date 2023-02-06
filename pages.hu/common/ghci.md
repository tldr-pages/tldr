# ghci

> A Glasgow Haskell Compiler interaktív környezete. További információ: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- Indítson el egy REPL-t (interaktív héj):

`ghci`

- REPL indítása és a megadott Haskell forrásfájl betöltése:

`ghci {{source_file.hs}}`

- REPL indítása és egy nyelvi opció engedélyezése:

`ghci -X{{language_option}}`

- Indítson el egy REPL-t és engedélyezze a fordítói figyelmeztetések bizonyos szintjét (pl. `all` vagy `compact`):

`ghci -W{{warning_level}}`

- REPL indítása a forrásfájlok keresésére szolgáló könyvtárak kettősponttal elválasztott listájával:

`ghci -i{{path/to/directory1}}:{{path/to/directory2}}`
