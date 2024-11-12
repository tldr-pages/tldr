# zint

> Genera códigos de barras y códigos QR.
> Más información: <https://www.zint.org.uk/manual/chapter/4>.

- Crea un archivo con un código de barras:

`zint --data "{{datos_UTF-8}}" --output {{ruta/al/archivo}}`

- Crea un archivo con otro tipo de código de barras:

`zint --barcode {{tipo_de_código}} --data "{{datos_UTF-8}}" --output {{ruta/al/archivo}}`

- Lista todos los tipos de códigos de barras soportados:

`zint --types`
