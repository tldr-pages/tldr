# zint

> CLI tool to generate various (bar/QR) codes.
> More information: <https://www.zint.org.uk/manual/chapter/4>.

- Generate a barcode and save it:

`zint --data {{your_data_in_utf8}} --output {{path/to/file}}`

- Specify a barcode type (list all possible values with `zint --types`) for generation:

`zint --barcode {{barcode_type}} --data {{your_data_in_utf8}} --output {{/path/to/file}}`
