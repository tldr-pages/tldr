# xzless

> Muestra texto de archivos comprimidos `xz` y `lzma`.
> Vea también: `less`.
> Más información: <https://manned.org/xzless>.

- Muestra un archivo comprimido:

`xzless {{ruta/al/archivo}}`

- Muestra un archivo comprimido incluyendo el números de línea:

`xzless --LINE-NUMBERS {{ruta/al/archivo}}`

- Muestra un archivo comprimido y sale si el archivo entero se puede mostrar en la primera pantalla:

`xzless --quit-if-one-screen {{ruta/al/archivo}}`
