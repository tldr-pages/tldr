# xbindkeys

> Grab key and mouse button events in X and run associated shell commands.
> More information: <https://manned.org/xbindkeys>.

- Start `xbindkeys` as a background daemon:

`xbindkeys`

- Generate the default configuration file:

`xbindkeys --defaults > ~/.xbindkeysrc`

- Identify a single key press to use in the configuration file:

`xbindkeys --key`

- Identify a multi-key press to use in the configuration file:

`xbindkeys --multikey`

- Use a specific configuration file instead of `~/.xbindkeysrc`:

`xbindkeys --file {{path/to/config_file}}`
