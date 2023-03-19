# assimp

> Cliente de línea de comandos para la biblioteca Open Asset Import.
> Admite la carga de más de 40 formatos de archivo 3D y la exportación a varios formatos 3D populares.
> Más información: <https://assimp-docs.readthedocs.io/>.

- Lista de todos los formatos de importación soportados:

`assimp listext`

- Lista de todos los formatos de exportación compatibles:

`assimp listexport`

- Convierte un archivo a uno de los formatos de salida soportados, utilizando los parámetros por defecto:

`assimp export {{archivo_entrada.stl}} {{archivo_salida.obj}}`

- Convertir un archivo utilizando parámetros personalizados (el archivo dox_cmd.h en el código fuente de assimp enumera los parámetros disponibles):

`assimp export {{archivo_entrada.stl}} {{archivo_salida.obj}} {{parametros}}`

- Muestra un resumen del contenido de un archivo 3D:

`assimp info {{ruta/al/archivo}}`

- Lista todos los subcomandos ("verbs") soportados:

`assimp help`

- Obtener ayuda sobre un subcomando concreto (por ejemplo, los parámetros específicos del mismo):

`assimp {{subcomando}} --help`
