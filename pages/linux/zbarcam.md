# zbarcam

> Scans and decodes barcodes (and QR codes) from a video device.
> More information: <https://manned.org/zbarcam>.

- Continuously read barcodes and print them to standard output:

`zbarcam`

- Disable output video window while scanning:

`zbarcam --nodisplay`

- Print barcodes without type information:

`zbarcam --raw`

- Define capture device:

`zbarcam /dev/{{video_device}}`
