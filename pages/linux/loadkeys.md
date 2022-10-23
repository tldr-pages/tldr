# loadkeys

> Load keyboard translation tables.
> More information: <https://manned.org/loadkeys.1>


- Loads the default keymap:

`loadkeys --default` \
`loadkeys defmap` (useful when a strange keymap is loaded and - sign cannot be found)

- Loads a keymap from the specified file for the console:

`loadkeys --console {{/path/to/console}} filename`

In Debian systems (like Ubuntu), install the package console-data using `sudo apt-get install console-data` and use standard names for keymaps of different locales (like `loadkeys --console {{/path/to/console}} uk`). Use root privilege if it shows an error like `could not open /path/to/console`.