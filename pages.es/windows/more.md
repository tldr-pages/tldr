# more

> Muestra la salida paginada desde `stdin` o un archivo.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Muestra la salida paginada desde `stdin`:

`{{echo prueba}} | more`

- Muestra la salida paginada desde uno o más archivos:

`more {{ruta\al\archivo}}`

- Convierte tabulaciones al número especificado de espacios:

`more {{ruta\al\archivo}} /t{{espacios}}`

- Limpia la pantalla antes de mostrar la página:

`more {{ruta\al\archivo}} /c`

- Muestra la salida comenzando en la línea 5:

`more {{ruta\al\archivo}} +{{5}}`

- Habilita el modo interactivo extendido (consulta la ayuda para su uso):

`more {{ruta\al\archivo}} /e`

- Muestra ayuda:

`more /?`
