# hexdump

> Un visor ASCII, decimal, hexadecimal, octal.
> Más información: <https://manned.org/hexdump>.

- Imprime la representación hexadecimal de un archivo, reemplazando líneas duplicadas con '*':

`hexdump {{ruta/al/archivo}}`

- Muestra el desplazamiento de entrada (input offset) en hexadecimal y su representación ASCII en dos columnas:

`hexdump {{[-C|--canonical]}} {{ruta/al/archivo}}`

- Muestra la representación hexadecimal de un archivo, pero interpreta solo n bytes de la entrada:

`hexdump {{[-C|--canonical]}} {{[-n|--length]}} {{número_de_bytes}} {{ruta/al/archivo}}`

- No reemplaza las líneas duplicadas con '*':

`hexdump {{[-v|--no-squeezing]}} {{ruta/al/archivo}}`
