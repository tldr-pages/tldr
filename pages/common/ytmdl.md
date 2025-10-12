# ytmdl

> Download songs from YouTube and automatically add metadata.
> Fetches song information (artist, album, cover art) from iTunes, Spotify, and other sources.
> More information: <https://github.com/deepjyoti30/ytmdl>.

- Download a song by name (with interactive selection):

`ytmdl "{{song name}}"`

- Download a song in quiet mode (automatically select the first result):

`ytmdl {{-q|--quiet}} "{{song name}}"`

- Download a song to a specific directory:

`ytmdl {{-o|--output-dir}} {{path/to/directory}} "{{song name}}"`

- Download a song from a YouTube URL:

`ytmdl --url "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Download a song in a specific format (mp3, m4a, or opus):

`ytmdl --format {{mp3}} "{{song name}}"`

- Download a song with artist and album information:

`ytmdl --artist "{{artist name}}" --album "{{album name}}" "{{song name}}"`

- Download a list of songs from a text file:

`ytmdl --list {{path/to/list.txt}}`

- Add metadata directly using an iTunes ID:

`ytmdl --itunes-id {{itunes_id}} "{{song name}}"`
