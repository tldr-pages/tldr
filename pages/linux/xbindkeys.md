# xbindkeys

> Grab keys and mouse buttons to run shell commands in X11.
> More information: <https://manned.org/xbindkeys>.

- Start the `xbindkeys` daemon:

`xbindkeys`

- Generate a default sample configuration file:

`xbindkeys --defaults > {{path/to/xbindkeysrc}}`

- Start `xbindkeys` using a specific configuration file:

`xbindkeys -f {{path/to/file}}`

- Interactively identify key codes and mouse button combinations:

`xbindkeys -k`

- Run `xbindkeys` in the foreground for debugging:

`xbindkeys -n -v`

- Reload configuration without restarting the daemon:

`xbindkeys -p`

- Display currently registered key bindings:

`xbindkeys --show`
