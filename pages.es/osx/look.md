# look

> Muestra las líneas que empiezan por un prefijo en un archivo ordenado.
> Vea también: `grep`, `sort`.
> Más información: <https://keith.github.io/xcode-man-pages/look.1.html>.

- Busca líneas que comiencen con un prefijo específico en un archivo específico:

`look {{prefijo}} {{ruta/al/archivo}}`

- Búsqueda insensible a mayúsculas y minúsculas solo en caracteres alfanuméricos:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefijo}} {{ruta/al/archivo}}`

- Especifica un carácter de terminación de cadena (espacio por defecto):

`look {{[-t|--terminate]}} {{,}}`

- Busca en `/usr/share/dict/words` (se asumen `--ignore-case` y `--alphanum`):

`look {{prefijo}}`
