# mid3v2

> Edit audio tags.
> See also: `id3v2`.
> More information: <https://mutagen.readthedocs.io/en/latest/man/mid3v2.html>.

- List all supported ID3v2.3 or ID3v2.4 frames and their meanings:

`mid3v2 --list-frames {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- List all supported ID3v1 numeric genres:

`mid3v2 --list-genres {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- List all tags in specific files:

`mid3v2 --list {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific artist, album, or song information:

`mid3v2 {{--artist|--album|--song}}={{string}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific picture information:

`mid3v2 --picture={{filename:description:image_type:mime_type}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific year information:

`mid3v2 --year={{YYYY}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Set specific date information:

`mid3v2 --date={{YYYY-MM-DD}} {{path/to/file1.mp3 path/to/file2.mp3 ...}}`
