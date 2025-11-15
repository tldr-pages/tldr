# where

> Muestra la ubicación de archivos que coinciden con el patrón de búsqueda.
> Por defecto busca en el directorio de trabajo actual y en las rutas definidas en la variable de entorno PATH.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- Muestra la ubicación del patrón de archivo:

`where {{patrón_de_archivo}}`

- Muestra la ubicación del patrón de archivo incluyendo tamaño y fecha:

`where /T {{patrón_de_archivo}}`

- Busca recursivamente el patrón de archivo en la ruta especificada:

`where /R {{ruta\al\directorio}} {{patrón_de_archivo}}`

- Retorna silenciosamente el código de error para la ubicación del patrón de archivo:

`where /Q {{patrón_de_archivo}}`
