# mid3v2

> Edit audio tags.
> See also: `id3v2`.
> More information: <https://manned.org/mid3v2.1>.

- List all supported ID3v2.3 or ID3v2.4 frames and their meanings:

`id3v2 --list-frames {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- List all supported ID3v1 numeric genres:

`id3v2 --list-genres {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- List all tags in specific files:

`id3v2 --list {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific artist, album, or song information:

`id3v2 {{--artist|--album|--song}}={{string}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific picture information:

`id3v2 --picture={{filename:description:image_type:mime_type}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific year information:

`id3v2 --year={{YYYY}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific date information:

`id3v2 --date={{YYYY-MM-DD}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`
