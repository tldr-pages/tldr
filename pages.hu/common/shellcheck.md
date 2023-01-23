# shellcheck

> Shell szkript statikus elemző eszköz. Ellenőrizze a shell szkripteket hibák, elavult/bizonytalan funkciók használata és rossz gyakorlatok szempontjából. További információ: <https://www.shellcheck.net>.

- Ellenőrizzen egy héjszkriptet:

`shellcheck {{path/to/script.sh}}`

- Ellenőrzi a megadott shell dialektusként értelmező shell scriptet (felülbírálja a shebanget a script elején):

`shellcheck --shell {{sh|bash|dash|ksh}} {{path/to/script.sh}}`

- Egy vagy több hibatípus figyelmen kívül hagyása:

`shellcheck --exclude {{SC1009,SC1073}} {{path/to/script.sh}}`

- Ellenőrizze a forrásként használt shell szkripteket is:

`shellcheck --checked-sourced {{path/to/script.sh}}`

- Kimenet megjelenítése a megadott formátumban (alapértelmezett: `tty`):

`shellcheck --format {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{path/to/script.sh}}`

- Egy vagy több opcionális ellenőrzés engedélyezése:

`shellcheck --enable={{add-default-case|avoid-nullary-conditions}}`

- Az összes elérhető opcionális ellenőrzés listázása, amelyek alapértelmezés szerint ki vannak kapcsolva:

`shellcheck --list-optional`
