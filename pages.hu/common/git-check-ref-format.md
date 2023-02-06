# git check-ref-format

> Ellenőrzi, hogy egy adott refname elfogadható-e, és nem nulla státusszal lép ki, ha nem. További információ: <https://git-scm.com/docs/git-check-ref-format>.

- A megadott refname formátumának ellenőrzése:

`git check-ref-format {{refs/head/refname}}`

- Kiírja az utoljára ellenőrzött ág nevét:

`git check-ref-format --branch @{-1}`

- Normalizálja a refnevet:

`git check-ref-format --normalize {{refs/head/refname}}`
