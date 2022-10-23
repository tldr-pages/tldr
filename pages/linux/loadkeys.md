# loadkeys

> Load keyboard translation tables.
> More information: <https://manned.org/loadkeys.1>.

- Load the default keymap:

`loadkeys --default`

- Load default keymap when an unusual keymap is loaded and - sign cannot be found:

`loadkeys defmap`

- Load a keymap from the specified file for the console:

`loadkeys --console {{/path/to/console}} filename`

- In Debian systems (like Ubuntu), install the package console-data using `sudo apt-get install console-data`. Then use standard names for keymaps of different locales:

`loadkeys --console {{path/to/console}} uk`
