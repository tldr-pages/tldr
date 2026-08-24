# find

> Busca archivos o directorios bajo una jerarquía de directorios.
> Vea también: `fd`.
> Más información: <https://manned.org/find>.

- Encuentra archivos por extensión:

`find {{ruta/al/directorio}} -name '{{*.ext}}'`

- Encuentra archivos que coinciden con múltiples patrones de ruta/nombre:

`find {{ruta/al/directorio}} -path '{{*/ruta/*/*.ext}}' -or -name '{{*patrón*}}'`

- Encuentra directorios que coinciden con un nombre dado, en modo insensible a mayúsculas y minúsculas:

`find {{ruta/al/directorio}} -type d -iname '{{*lib*}}'`

- Encuentra archivos que coinciden con un patrón dado, excluyendo rutas específicas:

`find {{ruta/al/directorio}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Encuentra archivos que coinciden con un rango de tamaño dado, limitando la profundidad recursiva a "1":

`find {{ruta/al/directorio}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Ejecuta un comando para cada archivo (usa `{}` dentro del comando para acceder al nombre del archivo):

`find {{ruta/al/directorio}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Encuentra todos los archivos modificados hoy y pasa los resultados a un solo comando como argumentos:

`find {{ruta/al/directorio}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Busca tanto archivos como directorios vacíos y los elimina detalladamente:

`find {{ruta/al/directorio}} -type {{f|d}} -empty -delete -print`
