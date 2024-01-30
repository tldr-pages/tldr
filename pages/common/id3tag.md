# id3tag

> Tool for reading, writing, and manipulating ID3v1 and ID3v2 tags of MP3 files.
> More information: <https://manned.org/id3tag>.

- Set artist and song title tag of an MP3 file:

`id3tag --artist {{artist}} --song {{song_title}} {{path/to/file.mp3}}`

- Set album title of all MP3 files in the current directory:

`id3tag --album={{album}} {{*.mp3}}`

- Display help:

`id3tag --help`
