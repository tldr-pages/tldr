# git check-attr

> Minden egyes elérési névhez listázza ki, hogy az egyes attribútumok meghatározatlanok, beállítottak vagy nem beállítottak-e gitattribútumként az adott elérési névben. További információ: <https://git-scm.com/docs/git-check-attr>.

- Ellenőrizze egy fájl összes attribútumának értékét:

`git check-attr --all {{path/to/file}}`

- Egy adott attribútum értékének ellenőrzése egy fájlban:

`git check-attr {{attribute}} {{path/to/file}}`

- Egy adott attribútum értékének ellenőrzése fájlokon:

`git check-attr --all {{path/to/file1}} {{path/to/file2}}`

- Egy adott attribútum értékének ellenőrzése egy vagy több fájlon:

`git check-attr {{attribute}} {{path/to/file1}} {{path/to/file2}}`
