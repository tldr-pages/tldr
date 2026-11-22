# rmpc

> A terminal music player client for the Music Player Daemon, with album art support.
> See also: `mpd`, `mpc`, `ncmpcpp`.
> More information: <https://rmpc.mierak.dev/reference/cli-command-mode/>.

- Start the TUI client:

`rmpc`

- Connect to a specific MPD instance:

`rmpc {{[-a|--address]}} {{host:port}}`

- Print the default configuration to use as a starting point:

`rmpc config`

- Scan the music directory for changes:

`rmpc update`

- Save the currently playing song's album art to a file:

`rmpc albumart {{[-o|--output]}} {{path/to/cover.jpg}}`

- Control playback (`toggleconsume` removes songs from the queue after they are played):

`rmpc {{next|prev|stop|togglepause|toggleconsume|togglerepeat}}`

- View the currently playing song:

`rmpc song`
