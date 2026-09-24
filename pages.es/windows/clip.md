# clip

> Copia el contenido de entrada al portapapeles de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Redirige la salida de la línea de comandos al portapapeles de Windows:

`{{dir}} | clip`

- Copia el contenido de un archivo al portapapeles de Windows:

`clip < {{ruta\al\archivo.ext}}`

- Copia texto con un salto de línea al portapapeles de Windows:

`echo {{texto}} | clip`

- Copia texto sin un salto de línea al portapapeles de Windows:

`echo | set /p="texto" | clip`
