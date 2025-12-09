# qrencode

> QR Code generator. Supports PNG and EPS.
> More information: <https://manned.org/qrencode>.

- Convert a string to a QR code and save to an output file:

`qrencode {{[-o|--output]}} {{path/to/output_file.png}} {{string}}`

- Convert an input file to a QR code and save to an output file:

`qrencode {{[-o|--output]}} {{path/to/output_file.png}} {{[-r|--read-from]}} {{path/to/input_file}}`

- Convert a string to a QR code and print it in terminal:

`qrencode {{[-t|--type]}} ansiutf8 {{string}}`

- Convert input from pipe to a QR code and print it in terminal:

`echo {{string}} | qrencode {{[-t|--type]}} ansiutf8`
