# pnmhisteq

> Ecualiza el histograma de una imagen PNM.
> Más información: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- Aumenta el contraste de una imagen PNM mediante la ecualización del histograma:

`pnmhisteq {{ruta/a/entrada.pnm}} > {{ruta/a/salida.pnm}}`

- Modifica solo los píxeles grises:

`pnmhisteq {{[-g|-grey]}} {{ruta/a/entrada.pnm}} > {{ruta/a/salida.pnm}}`

- No incluye píxeles negros ni blancos en la ecualización del histograma:

`pnmhisteq -no{{black|white}} {{ruta/a/entrada.pnm}} > {{ruta/a/salida.pnm}}`
