# tic

> Compilați terminfo și instalați pentru ncurses.
> Mai multe informaţii: <https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>

- Compilarea și instalarea terminfo pentru un terminal:

`tic -xe {{terminal}} {{path/to/terminal.info}}`

- Verificați fișierul terminfo pentru erori:

`tic -c {{path/to/terminal.info}}`

- Imprimarea locațiilor bazei de date

`tic -D`
