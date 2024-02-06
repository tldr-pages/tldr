# look

> Muestra las líneas que empiezan con un prefijo en un archivo ordenado.
> Vea también: `grep`, `sort`.
> Más información: <https://man.freebsd.org/cgi/man.cgi?look>.

- Busca líneas que comiencen con un prefijo específico en un archivo específico:

`look {{prefijo}} {{ruta/al/archivo}}`

- Busca caracteres alfanuméricos sin tomar en cuenta las mayúsculas o minúsculas:

`look -{{f|-ignore-case}} -{{d|-alphanum}} {{prefijo}} {{ruta/al/archivo}}`

- Especifica un carácter de [t]erminación de cadena (un espacio por defecto):

`look -{{t|-terminate}} {{,}}`

- Busca en `/usr/share/dict/words` (se asumen `--ignore-case` y `--alphanum`):

`look {{prefijo}}`
