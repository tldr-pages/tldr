# box

> PHP-alkalmazás a Pharok építésére és kezelésére. További információ: <https://github.com/box-project/box>.

- Fordítson le egy új Phar fájlt:

`box compile`

- Új Phar fájl fordítása egy adott konfigurációs fájl segítségével:

`box compile -c {{path/to/config}}`

- A PHAR PHP-bővítményre vonatkozó információk megjelenítése:

`box info`

- Egy adott Phar fájlról szóló információk megjelenítése:

`box info {{path/to/phar_file}}`

- A munkakönyvtárban elsőként megtalált konfigurációs fájl érvényesítése:

`box validate`

- Egy adott Phar fájl aláírásának ellenőrzése:

`box verify {{path/to/phar_file}}`

- Az összes elérhető parancs és opció megjelenítése:

`box help`
