# cdparanoia

> Extract audio tracks from CDs.
> More information: <https://xiph.org/paranoia/index.html>.

- Extract all tracks and write them into separate WAV files named `track#.wav`:

`cdparanoia {{[-B|--batch]}}`

- Print the CD's table of contents to the terminal:

`cdparanoia {{[-Q|--query]}}`

- Extract tracks 2 to 5 and write them into a single WAV file:

`cdparanoia 2-5`

- Extract track 3 and write it into a file called `path/to/file.wav`:

`cdparanoia 3 '{{path/to/file.wav}}'`
