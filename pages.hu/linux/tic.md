# tic

> Terminfo fordítása és telepítése az ncurses számára. További információ: <https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>.

- Terminfo fordítása és telepítése terminálhoz:

`tic -xe {{terminal}} {{path/to/terminal.info}}`

- A terminfo fájl hibaellenőrzése:

`tic -c {{path/to/terminal.info}}`

- Adatbázisok helyének nyomtatása:

`tic -D`
