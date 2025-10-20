# ytmdl

> Download songs from YouTube and automatically add metadata.
> Fetch song information (artist, album, cover art) from iTunes, Spotify, and other sources.
> More information: <https://github.com/deepjyoti30/ytmdl#usage>.

- Download a song by name (with interactive selection):

`ytmdl {{song_name}}`

- Download the first result without prompting:

`ytmdl {{[-q|--quiet]}} {{song_name}}`

- Download a song to a specific directory:

`ytmdl {{[-o|--output-dir]}} {{path/to/directory}} {{song_name}}`

- Download a song from a YouTube URL:

`ytmdl --url https://www.youtube.com/watch?v={{oHg5SJYRHA0}}`

- Download a song in a specific format (mp3, m4a, or opus):

`ytmdl --format {{mp3|m4a|opus}} {{song_name}}`

- Download a song with artist and album information:

`ytmdl --artist {{artist_name}} --album {{album_name}} {{song_name}}`

- Download a list of songs from a text file:

`ytmdl --list {{path/to/list.txt}}`

- Display help:

`ytmdl {{[-h|--help]}}`
