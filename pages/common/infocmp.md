# infocmp

> Display and compare terminal capability descriptions from the terminfo database.
> See also: `tput`, `tic`.
> More information: <https://invisible-island.net/ncurses/man/infocmp.1m.html>.

- Display the terminfo description for the current terminal:

`infocmp`

- Display the description for a specific terminal type:

`infocmp {{xterm-256color}}`

- Display one capability per line:

`infocmp -1 {{xterm-256color}}`

- Display long capability names instead of terminfo codes:

`infocmp -L {{xterm-256color}}`

- List [d]ifferences between two terminal types:

`infocmp -d {{xterm}} {{xterm-256color}}`

- Display a terminal description using term[C]ap capability names:

`infocmp -C {{xterm}}`
