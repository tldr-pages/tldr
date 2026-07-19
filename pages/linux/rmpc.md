# rmpc

> A modern terminal Music Player Daemon (MPD) client with album art support.
> See also: `ncmpcpp`, `mpc`, `mpd`.
> More information: <https://rmpc.mierak.dev>.

- Start the interactive client:

`rmpc`

- Connect to a specific MPD address:

`rmpc {{[-a|--address]}} {{ip_address:port}}`

- Toggle play/pause:

`rmpc togglepause`

- Play the next or previous song:

`rmpc {{next|prev}}`

- Set or print the current volume:

`rmpc volume {{volume}}`

- Add a path from the music library to the queue:

`rmpc add {{path/to/song_or_directory}}`

- Save the current song's album art to a file:

`rmpc albumart {{[-o|--output]}} {{path/to/cover.png}}`

- Print the default config to bootstrap a config file:

`rmpc config`
