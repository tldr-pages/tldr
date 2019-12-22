# clear

> Clears the screen of the terminal.

- Clear the screen (equivalent to pressing Control-L in Bash shell):

`clear`

- Clear the screen but keep the terminal's scrollback buffer:

`clear -x`

- Indicate the type of terminal to clean (normally this option is unnecessary because it is taken from the environment variable `TERM`):

`clear -T {type_of_terminal}`

- Show the version of `ncurses` used by `clear`:

`clear -V`
