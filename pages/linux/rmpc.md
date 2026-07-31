# rmpc

> A terminal music player client for the Music Player Daemon, with album art support.
> See also: `mpd`, `mpc`, `ncmpcpp`.
> More information: <https://rmpc.mierak.dev>.

- Start the TUI client:

`rmpc`

- Connect to a specific MPD instance:

`rmpc --address {{host:port}}`

- Print the default configuration to use as a starting point:

`rmpc config`

- Scan the music directory for changes:

`rmpc update`

- Save the currently playing song's album art to a file:

`rmpc albumart --output {{path/to/cover.jpg}}`

- Toggle playback control functions (consume plays the song and deletes it from the queque afterwards.):

`rmpc {{next|prev|stop|consume|togglerepeat|pause|unpause}}`

- View currently playing song:

`rmpc song`
