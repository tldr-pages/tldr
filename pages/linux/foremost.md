# foremost

> Recover files using their headers, footers, and data structures.
> More information: <https://foremost.sourceforge.net/>.

- Recover all supported file types from a disk image:

`foremost -i {{path/to/image.dd}}`

- Recover only JPEG files, skipping the first 100 blocks:

`foremost -s 100 -t {{jpg}} -i {{path/to/image.dd}}`

- Recover GIF and PDF files from a disk image:

`foremost -t {{gif,pdf}} -i {{path/to/image.dd}}`

- Save recovered files to a specific output directory:

`foremost -o {{path/to/output_directory}} -i {{path/to/image.dd}}`

- Recover Office documents and JPEG files in verbose mode with indirect block detection enabled:

`foremost -v -d -t {{ole,jpg}} -i {{path/to/image.dd}}`
