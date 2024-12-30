# zbarcam

> Escanea y decodifica códigos de barras (y códigos QR) desde un dispositivo de vídeo.
> Más información: <https://manned.org/zbarcam>.

- Lee continuamente códigos de barras y los imprime a `stdout`:

`zbarcam`

- Desactiva la ventana de salida de video mientras se escanea:

`zbarcam --nodisplay`

- Imprime códigos de barras sin información de tipo:

`zbarcam --raw`

- Define el dispositivo de captura:

`zbarcam {{/dev/dispositivo_de_video}}`
