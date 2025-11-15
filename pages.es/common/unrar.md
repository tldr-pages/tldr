# unrar

> Extrae archivos RAR.
> Más información: <https://manned.org/unrar>.

- Extrae archivos comprimidos respetando la estructura original del archivo:

`unrar x {{archivo_comprimido.rar}}`

- Extrae archivos comprimidos en una ruta determinada respetando la estructura original del archivo:

`unrar x {{archivo_comprimido.rar}} {{ruta/donde/extraer}}`

- Extrae archivos comprimidos en el directorio actual, perdiendo la estructura original del archivo:

`unrar e {{archivo_comprimido.rar}}`

- Comprueba la integridad de cada uno de los archivos dentro del archivo comprimido:

`unrar t {{archivo_comprimido.rar}}`

- Muestra el listado de los archivos dentro del archivo comprimido sin descomprimirlo:

`unrar l {{archivo_comprimido.rar}}`
