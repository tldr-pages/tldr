# qr

> Generate QR codes in the terminal with ANSI VT-100 escape codes.
> More information: <https://manned.org/qr>.

- Generate a QR code:

`qr "{{data}}"`

- Specify the error correction level (defaults to `M`):

`qr --error-correction {{L|M|Q|H}} "{{data}}"`

- Generate a QR code from the output of another command:

`{{command}} | qr`

- Save the QR code as a PNG image:

`qr "{{data}}" > {{path/to/file.png}}`
