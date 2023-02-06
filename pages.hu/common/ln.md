# ln

> Linkeket hoz létre fájlokra és könyvtárakra. További információ: <https://www.gnu.org/software/coreutils/ln>.

- Szimbolikus hivatkozás létrehozása egy fájlhoz vagy könyvtárhoz:

`ln -s {{/path/to/file_or_directory}} {{path/to/symlink}}`

- Egy meglévő szimbolikus link felülírása, hogy egy másik fájlra mutasson:

`ln -sf {{/path/to/new_file}} {{path/to/symlink}}`

- Kemény hivatkozás létrehozása egy fájlhoz:

`ln {{/path/to/file}} {{path/to/hardlink}}`
