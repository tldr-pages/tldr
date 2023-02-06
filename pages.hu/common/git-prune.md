# git prune

> Git parancs az elérhetetlen objektumok metszésére az objektum adatbázisból. Ezt a parancsot gyakran nem közvetlenül használják, hanem egy belső parancsként, amelyet a Git gc használ. További információ: <https://git-scm.com/docs/git-prune>.

- Jelentse, hogy mit távolítana el a Git prune anélkül, hogy eltávolítaná:

`git prune --dry-run`

- Az elérhetetlen objektumok metszése és annak megjelenítése, hogy mi lett metszve a `stdout`:

`git prune --verbose`

- Elérhetetlen objektumok metszése a haladás megjelenítése mellett:

`git prune --progress`
