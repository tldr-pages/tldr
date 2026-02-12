# od

> Muestra el contenido del archivo en formato octal, decimal o hexadecimal.
> Opcionalmente, muestra las compensaciones de bytes y/o la representación imprimible de cada línea.
> Vea también: `hexyl`, `xxd`, `hexdump`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- Muestra el archivo con la configuración predeterminada: formato octal, 8 bytes por línea, desplazamientos de bytes en octal y líneas duplicadas sustituidas por `*`:

`od {{ruta/al/archivo}}`

- Muestra el archivo en modo detallado, es decir, sin sustituir las líneas duplicadas por `*`:

`od {{[-v|--output-duplicates]}} {{ruta/al/archivo}}`

- Muestra el archivo en formato hexadecimal (unidades de 2 bytes), con desplazamientos de bytes en formato decimal:

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{ruta/al/archivo}}`

- Muestra el archivo en formato hexadecimal (unidades de 1 byte) y 4 bytes por línea:

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}4 {{[-v|--output-duplicates]}} {{ruta/al/archivo}}`

- Muestra el archivo en formato hexadecimal junto con su representación en caracteres y no imprime las compensaciones de bytes:

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{ruta/al/archivo}}`

- Lee solo 100 bytes de un archivo a partir del byte 500:

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{ruta/al/archivo}}`
