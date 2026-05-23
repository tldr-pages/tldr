# rmpc

> A configurable terminal-based Music Player Daemon client with album art support.
> See also: `mpd`, `mpc`, `ncmpcpp`.
> More information: <https://rmpc.mierak.dev/overview/>.

- Start the interactive terminal UI:

`rmpc`

- Start the UI and connect to a specific MPD address:

`rmpc {{[-a|--address]}} {{127.0.0.1:6600}}`

- Toggle playback or skip to another track:

`rmpc {{togglepause|next|prev}}`

- Display playback status or information about the current song:

`rmpc {{status|song}}`

- Add a song to the queue using a path relative to MPD's music directory:

`rmpc add {{path/to/song}}`

- Update MPD's music database:

`rmpc {{update|rescan}}`

- Save the current album art to a file:

`rmpc albumart {{[-o|--output]}} {{path/to/file}}`

- Skip to the next track in a running `rmpc` instance using the default keybind:

`rmpc remote keybind ">"`
