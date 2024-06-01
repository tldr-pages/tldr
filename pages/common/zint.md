# zint

> Generate barcodes and QR codes.
> More information: <https://www.zint.org.uk/manual/chapter/4>.

- Generate a barcode and save it:

`zint --data "{{UTF-8 data}}" --output {{path/to/file}}`

- Specify a barcode type (list all possible values with `zint --types`) for generation:

`zint --barcode {{barcode_type}} --data "{{UTF-8 data}}" --output {{path/to/file}}`
