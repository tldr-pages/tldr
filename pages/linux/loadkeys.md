# loadkeys

> Load the kernel keymap for the console.
> See also: `localectl`.
> More information: <https://manned.org/loadkeys>.

- Load a specific keyboard layout for the current console:

`sudo loadkeys {{en|de|fi|dvorak|defkeymap|...}}`

- Load a default keymap:

`sudo loadkeys {{[-d|--default]}}`

- Create a kernel source table:

`loadkeys {{[-m|--mktable]}}`

- Create a binary keymap:

`loadkeys {{[-b|--bkeymap]}}`

- Search and parse keymap without action:

`loadkeys {{[-p|--parse]}}`

- Load the keymap suppressing all output:

`loadkeys {{[-q|--quiet]}}`

- Set a keymap for a specific console:

`sudo loadkeys {{[-C|--console]}} {{/dev/ttyN}} {{uk}}`

- Load a keymap from the specified file for the console:

`loadkeys {{[-C|--console]}} {{/dev/ttyN}} /{{path/to/file}}`
