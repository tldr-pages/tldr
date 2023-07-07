# cavif

> PNG/JPEG to AVIF converter
> More information: <https://github.com/kornelski/cavif-rs>.

- Convert a JPEG file to AVIF:

`cavif {{path/to/filename.jpg}}`

- Set the destination filename explicitly:

`cavif {{path/to/filename.jpg}} --output {{path/to/filename.avif}}`

- Overwrite the destination file if it already exists:

`cavif --overwrite {{path/to/filename.jpg}}`
