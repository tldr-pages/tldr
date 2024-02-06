# look

> Muestra las líneas que empiezan por un prefijo en un archivo ordenado.
> Vea también: `grep`, `sort`.
> Más información: <https://man.freebsd.org/cgi/man.cgi?look>.

- Busca líneas que comiencen con un prefijo específico en un archivo específico:

`look {{prefijo}} {{ruta/al/archivo}}`

- Búsqueda insensible a mayúsculas y minúsculas sólo en caracteres alfanuméricos:

`look -{{f|-ignore-case}} -{{d|-alphanum}} {{prefijo}} {{ruta/al/archivo}}`

- Especifica un carácter de [t]erminación de cadena (espacio por defecto):

`look -{{t|-terminate}} {{,}}`

- Busca en `/usr/share/dict/words` (se asumen `--ignore-case` y `--alphanum`):

`look {{prefijo}}`
