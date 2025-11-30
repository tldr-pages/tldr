# clear

> Clears the screen of the terminal.
> More information: <https://manned.org/clear>.

- Clear the screen:

`clear`

- Clear the screen but keep the terminal's scrollback buffer (equivalent to pressing `<Ctrl l>` in Bash):

`clear -x`

- Indicate the type of terminal to clean (defaults to the value of the environment variable `$TERM`):

`clear -T {{type_of_terminal}}`

- Display the version of `ncurses` used by `clear`:

`clear -V`
