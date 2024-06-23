# zint

> Generate barcodes and QR codes.
> More information: <https://www.zint.org.uk/manual/chapter/4>.

- Generate a barcode and save it:

`zint --data "{{UTF-8 data}}" --output {{path/to/file}}`

- Specify a code type for generation:

`zint --barcode {{code_type}} --data "{{UTF-8 data}}" --output {{path/to/file}}`

- List all supported code types:

`zint --types`
