# scd

> A tiny file manager focused on shell integration.
> More information: <https://github.com/cshuaimin/scd>.

- Recursively index some paths for the very first run:

`scd -ar {{path/to/directory}}`

- Change to a directory path:

`scd {{path/to/directory}}`

To change to a path matching all of "a", "b" and "c":

`scd {{a}} {{b}} {{c}}`

- change to a directory path that ends with "ts":

`scd "ts$"`

- Show selection menu and ranking of 20 most likely directories:

`scd -v`

- Alias current directory as {{name}}:

`scd --alias={{name}}`

- Jump to directory with previously defined alias {{name}}:

`scd {{name}}`
