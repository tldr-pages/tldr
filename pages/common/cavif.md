# cavif

> PNG/JPEG to AVIF converter. Written in Rust.
> See also: `convert`.
> More information: <https://github.com/kornelski/cavif-rs>.

- Convert a JPEG file to AVIF, saving it to `file.avif`:

`cavif {{path/to/file.jpg}}`

- Adjust the image quality (1-100) and convert a PNG file to AVIF:

`cavif --quality {{60}} {{path/to/file.png}}`

- Specify the output location:

`cavif {{path/to/file.jpg}} --output {{path/to/file.avif}}`

- Overwrite the destination file if it already exists:

`cavif --overwrite {{path/to/file.jpg}}`
