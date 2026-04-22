# xbindkeys

> Bind commands to keyboard keys and mouse buttons in X.
> See also: `xev`, `xmodmap`.
> More information: <https://manned.org/xbindkeys>.

- Start `xbindkeys` in the background using the default configuration file:

`xbindkeys`

- Start `xbindkeys` in the foreground and print debug output:

`xbindkeys --nodaemon --verbose`

- Print a default configuration file:

`xbindkeys --defaults`

- Identify a key or mouse button to use in a binding:

`xbindkeys --key`

- Identify a multi-key chord to use in a binding:

`xbindkeys --multikey`

- Load bindings from an alternative configuration file:

`xbindkeys --file {{path/to/config_file}}`
