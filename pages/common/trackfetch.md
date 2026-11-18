# trackfetch

> Download songs listed in a text file or passed as arguments, saving them as tagged MP3, M4A, or Opus files using configurable metadata sources and YouTube audio.
> Requires `yt-dlp`, `ffmpeg`, and `deno`. Spotify is optional and only used when selected.
> More information: <https://github.com/ByteMe6/trackfetch#usage>.

- Download every song from a file with one `Artist - Title` per line into the current directory:

`trackfetch {{path/to/songs.txt}}`

- Download songs into a specific directory:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Download one or more tracks passed as arguments instead of a text file:

`trackfetch {{"Artist1 - Title1" "Artist2 - Title2" ...}}`

- Choose which metadata sources to use (the default is `itunes`):

`trackfetch {{path/to/songs.txt}} {{[-s|--metadata-sources]}} {{deezer,itunes,musicbrainz}}`

- Choose the output format (the default is `m4a`; `m4a` and `opus` keep YouTube's original audio):

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{mp3|m4a|opus}}`

- Use a config file for the defaults:

`trackfetch {{path/to/songs.txt}} --config {{path/to/config.ini}}`

- Wait a number of seconds between songs to avoid rate limiting:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Retry the songs that failed in a previous run:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt >{{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
