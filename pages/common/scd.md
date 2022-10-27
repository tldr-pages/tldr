# scd

> File manager focused on shell integration.
> More information: <https://github.com/cshuaimin/scd>.

- Index paths recursively for the very first run:

`scd -ar {{path/to/directory}}`

- Change to a directory path:

`scd {{path/to/directory}}`

- Change to a path matching all of "a", "b" and "c":

`scd {{a}} {{b}} {{c}}`

- Change to a directory path that ends with "ts":

`scd "ts$"`

- Show selection menu and ranking of 20 most likely directories:

`scd -v`

- Add an alias for the current directory:

`scd --alias={{name}}`

- Jump to a directory with a previously defined alias:

`scd {{word}}`
