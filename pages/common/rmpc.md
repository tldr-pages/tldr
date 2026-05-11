# rmpc

> A terminal music player client for the Music Player Daemon, with album art support.
> See also: `mpd`, `mpc`, `ncmpcpp`.
> More information: <https://rmpc.mierak.dev>.

- Start the TUI client:

`rmpc`

- Connect to a specific MPD instance:

`rmpc --address {{host:port}}`

- Toggle between play and pause:

`rmpc togglepause`

- Play the next or previous song:

`rmpc {{next|prev}}`

- Scan the music directory for changes:

`rmpc update`

- Save the currently playing song's album art to a file:

`rmpc albumart --output {{path/to/cover.jpg}}`

- Print the default configuration to use as a starting point:

`rmpc config`
