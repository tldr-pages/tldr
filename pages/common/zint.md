# zint

> CLI tool to generate various (bar/QR) codes
> More information: <https://www.zint.org.uk/manual/chapter/4>.

- Generate a barcode and save it:

`zint -d {{your_data_in_utf8}} -o {{/path/to/file}}`

- Specify a barcode type (list all possibler values with `zint -t` for generation:

`zint -b {{barcode_type}} -d {{your_data_in_utf8}} -o {{/path/to/file}}`
