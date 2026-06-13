# loadkeys

> Load the kernel keymap for the console.
> See also: `localectl`.
> More information: <https://manned.org/loadkeys>.

- Load a specific keyboard layout for the current console:

`sudo loadkeys {{en|de|fi|dvorak|defkeymap|...}}`

- Load a default keymap:

`sudo loadkeys {{[-d|--default]}}`

- Print the kernel source table of a keymap to `stdout`:

`loadkeys {{[-m|--mktable]}} {{en|de|fi|...}}`

- Print the binary format of a keymap to `stdout`:

`loadkeys {{[-b|--bkeymap]}} {{en|de|fi|...}}`

- Search and parse keymap without action:

`loadkeys {{[-p|--parse]}} {{en|de|fi|...}}`

- Load a keymap from `stdin`, suppressing all output:

`{{command}} | sudo loadkeys {{[-q|--quiet]}}`

- Set a keymap for a specific console:

`sudo loadkeys {{[-C|--console]}} {{/dev/ttyN}} {{uk}}`

- Load a keymap from the specified file for the console:

`sudo loadkeys {{[-C|--console]}} {{/dev/ttyN}} /{{path/to/file}}`
