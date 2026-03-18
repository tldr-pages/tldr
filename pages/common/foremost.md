# foremost

> Recover files from a disk image or device based on file headers and footers.
> More information: <https://foremost.sourceforge.net>.

- Recover all supported file types from a disk image:

`foremost -i {{path/to/image.dd}}`

- Recover specific file [t]ypes from a disk image:

`foremost -i {{path/to/image.dd}} -t {{jpeg,pdf,png}}`

- Recover files and write results to a specific [o]utput directory:

`foremost -i {{path/to/image.dd}} -o {{path/to/output_directory}}`

- Recover files from a device with [v]erbose output:

`foremost -v -i {{/dev/sdXY}}`

- Recover all headers without error detection (useful for corrupted files):

`foremost -a -i {{path/to/image.dd}}`

- Perform a [q]uick scan using 512-byte boundary searches:

`foremost -q -i {{path/to/image.dd}}`

- Only generate the audit file without writing recovered files:

`foremost -w -i {{path/to/image.dd}} -o {{path/to/output_directory}}`

- Use a custom [c]onfiguration file:

`foremost -c {{path/to/foremost.conf}} -i {{path/to/image.dd}}`
