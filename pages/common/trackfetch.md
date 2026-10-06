# trackfetch

> Download songs listed in a text file as tagged MP3 files, using Spotify metadata and YouTube audio.
> Requires `yt-dlp`, `ffmpeg` and the `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` environment variables.
> More information: <https://github.com/ByteMe6/trackfetch#usage>.

- Download every song from a file with one `Artist - Title` per line into `~/Music/trackfetch`:

`trackfetch {{path/to/songs.txt}}`

- Download songs into a specific directory:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Name the files by song title only, instead of `Artist - Title`:

`trackfetch {{path/to/songs.txt}} --title-only`

- Wait a number of seconds between songs to avoid rate limiting:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Retry the songs that failed in a previous run:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Display help:

`trackfetch {{[-h|--help]}}`
