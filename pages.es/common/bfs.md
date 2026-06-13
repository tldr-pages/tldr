# bfs

> Búsqueda exhaustiva de tus archivos.
> Más información: <https://manned.org/bfs>.

- Busca archivos por extensión:

`bfs {{ruta_raíz}} -name '{{*.ext}}'`

- Busca archivos que coincidan con varios patrones de ruta/nombre:

`bfs {{ruta_raíz}} -path '{{**/ruta/**/*.ext}}' -or -name '{{*patrón*}}'`

- Busca directorios que coincidan con un nombre dado, sin distinguir mayúsculas de minúsculas:

`bfs {{ruta_raíz}} -type d -iname '{{*lib*}}'`

- Busca archivos que coincidan con un patrón dado, excluyendo rutas específicas:

`bfs {{ruta_raíz}} -name '{{*.py}}' -not -path '{{*/paquetes/*}}'`

- Busca archivos que coincidan con un rango de tamaño dado, limitando la profundidad recursiva a "1":

`bfs {{ruta_raíz}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Ejecuta un comando para cada archivo (utiliza `{}` dentro del comando para acceder al nombre del archivo):

`bfs {{ruta_root}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Busca todos los archivos modificados hoy y pasa los resultados a un único comando como argumentos:

`bfs {{ruta_raíz}} -daystart -mtime {{-1}} -exec {{tar -cvf archivo.tar}} {} \+`

- Encuentra archivos vacíos (0 bytes) o directorios y los elimina de forma detallada:

`bfs {{ruta_raíz}} -type {{f|d}} -empty -delete -print`
