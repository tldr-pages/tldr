# git stripspace

> Szövegek (pl. commit üzenetek, jegyzetek, címkék és ágleírások) beolvasása a standard bemenetről, és tisztítása a Git által használt módon. További információ: <https://git-scm.com/docs/git-stripspace>.

- A szóközök levágása egy fájlból:

`cat {{path/to/file}} | git stripspace`

- A szóközök és a Git-kommentárok levágása egy fájlból:

`cat {{path/to/file}} | git stripspace --strip-comments`

- Egy fájl összes sorának Git-kommentárrá alakítása:

`git stripspace --comment-lines < {{path/to/file}}`
