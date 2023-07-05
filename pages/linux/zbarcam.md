# zbarcam

> Scans and decodes barcodes from a video device.
> More information: <https://linux.die.net/man/1/zbarcam>.

- Continuously read barcodes and print them to standard output:

`zbarcam`

- Disable output video window while scanning:

`zbarcam --nodisplay`

- Print barcodes without type information:

`zbarcam --raw`

- Define capture device:

`zbarcam /dev/{{video_device}}`
