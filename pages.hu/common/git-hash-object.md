# git hash-object

> Kiszámítja a tartalom egyedi hash-kulcsát, és opcionálisan létrehoz egy objektumot a megadott típussal. További információ: <https://git-scm.com/docs/git-hash-object>.

- Az objektum azonosítójának kiszámítása tárolás nélkül:

`git hash-object {{path/to/file}}`

- Kiszámítja az objektum azonosítóját és tárolja a Git adatbázisban:

`git hash-object -w {{path/to/file}}`

- Az objektum azonosítójának kiszámítása az objektum típusának megadásával:

`git hash-object -t {{blob|commit|tag|tree}} {{path/to/file}}`

- Az objektum azonosítójának kiszámítása a `stdin`:

`cat {{path/to/file}} | git hash-object --stdin`
