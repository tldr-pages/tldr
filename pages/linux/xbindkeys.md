# xbindkeys

> Associate keyboard keys and mouse buttons with shell commands in X11.
> More information: <https://manned.org/xbindkeys>.

- Start xbindkeys as a background daemon:

`xbindkeys`

- Generate a default configuration file:

`xbindkeys --defaults > ~/.xbindkeysrc`

- Start xbindkeys with a specific configuration file:

`xbindkeys --file {{path/to/config_file}}`

- Identify a key combination interactively:

`xbindkeys --key`

- Identify multiple sequential key combinations:

`xbindkeys --multikey`

- Run xbindkeys in the foreground with verbose diagnostic output:

`xbindkeys --nodaemon --verbose`

- Show the currently configured keybindings:

`xbindkeys --show`
