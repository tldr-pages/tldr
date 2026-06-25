# clementine

> A modern music player and library organizer.
> See also: `audacious`, `qmmp`, `cmus`, `mpv`.
> More information: <https://manned.org/clementine>.

- Start the GUI or bring it to front:

`clementine`

- Start playing music:

`clementine {{url|path/to/music.ext}}`

- Toggle between pausing and playing:

`clementine {{[-t|--play-pause]}}`

- Stop playback:

`clementine {{[-s|--stop]}}`

- Skip to the next or previous track:

`clementine --{{next|previous}}`

- Create a new playlist with one or more music files or URLs:

`clementine {{[-c|--create]}} {{url1|path/to/music1.ext url2|path/to/music2.ext ...}}`

- Load a playlist file:

`clementine {{[-l|--load]}} {{path/to/playlist.ext}}`

- Play a specific track in the currently loaded playlist:

`clementine {{[-k|--play-track]}} {{5}}`
