# tic

> Compile terminfo and install for ncurses.
> More information: <https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>.

- Compile and install terminfo for a terminal:

`tic -xe {{terminal}} {{path/to/terminal.info}}`

- Check terminfo file for errors:

`tic -c {{path/to/terminal.info}}`

- Print database locations:

`tic -D`
