# es

> Interfaz de línea de comandos para Everything, una herramienta de búsqueda rápida de archivos y carpetas para Windows.
> Requiere que Everything esté instalado y ejecutándose en segundo plano.
> Más información: <https://www.voidtools.com/support/everything/command_line_interface/>.

- Busca un archivo o carpeta por su nombre:

`es {{término_de_búsqueda}}`

- Busca usando una expresión regular:

`es -r {{patrón_regex}}`

- Busca palabras completas:

`es -w {{término_de_búsqueda}}`

- Limita el número de resultados mostrados:

`es -n {{10}} {{término_de_búsqueda}}`

- Busca dentro de una carpeta específica:

`es -path {{ruta_de_la_carpeta}} {{término_de_búsqueda}}`

- Lista solo carpetas:

`es /ad`

- Lista solo archivos:

`es /a-d`

- Ordena los resultados (por ejemplo, por nombre):

`es -sort {{nombre-ascendente}}`
