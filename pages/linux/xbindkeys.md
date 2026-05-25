# xbindkeys

> Associate commands with keyboard shortcuts in X.
> More information: <https://www.nongnu.org/xbindkeys/xbindkeys.html>.

- Create a default configuration file in the home directory:

`xbindkeys --defaults > ~/.xbindkeysrc`

- Start xbindkeys with the default configuration file:

`xbindkeys`

- Reload the configuration file without restarting xbindkeys:

`killall -HUP xbindkeys`

- Show the keycodes of pressed keys:

`xbindkeys --key`

- Display help:

`xbindkeys --help`
