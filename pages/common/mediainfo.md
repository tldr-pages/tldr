# mediainfo

> Display metadata from video and audio files.
> More information: <https://mediaarea.net/MediaInfo>.

- Display metadata for a given file in the console:

`mediainfo {{path/to/file}}`

- Store the output to a given file along with displaying in the console:

`mediainfo --Logfile={{out.txt}} {{path/to/file}}`

- Display the list of metadata attributes that can be extracted:

`mediainfo --Info-Parameters`
