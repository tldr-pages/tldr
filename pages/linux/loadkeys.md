# loadkeys

> Load the kernel keymap for the console.
> More information: <https://manned.org/loadkeys>.

- Load a default keymap:

`loadkeys {{[-d|--default]}}`

- Load default keymap when an unusual keymap is loaded and `-` sign cannot be found:

`loadkeys defmap`

- Create a kernel source table:

`loadkeys {{[-m|--mktable]}}`

- Create a binary keymap:

`loadkeys {{[-b|--bkeymap]}}`

- Search and parse keymap without action:

`loadkeys {{[-p|--parse]}}`

- Load the keymap suppressing all output:

`loadkeys {{[-q|--quiet]}}`

- Load a keymap from the specified file for the console:

`loadkeys {{[-C|--console]}} {{/dev/ttyN}} {{/path/to/file}}`

- Use standard names for keymaps of different locales:

`loadkeys {{[-C|--console]}} {{/dev/ttyN}} {{uk}}`
