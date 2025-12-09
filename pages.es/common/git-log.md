# git log

> Muestra un historial de confirmaciones.
> Más información: <https://git-scm.com/docs/git-log>.

- Muestra la secuencia de confirmaciones comenzando desde el actual, en orden cronológico inverso, del respositorio de Git en el directorio de trabajo actual:

`git log`

- Muestra el historial de un archivo o directorio específico, incluyendo las diferencias:

`git log {{[-p|--patch]}} {{ruta/al/archivo_o_directorio}}`

- Muestra un resumen de los archivos, o archivo, cambiados en cada confirmación:

`git log --stat`

- Muestra un gráfico de las confirmaciones en la rama actual, utilizando solo la primer línea del mensaje de cada uno:

`git log --oneline --graph`

- Muestra un gráfico de todos las confirmaciones, etiquetas y ramas en todo el repositorio:

`git log --oneline --decorate --all --graph`

- Muestra solo las confirmaciones cuyo mensaje incluye una cadena dada (no diferencia entre mayúsculas y minúsculas):

`git log {{[-i|--regexp-ignore-case]}} --grep {{cadena_a_buscar}}`

- Muestra las últimas N confirmaciones de determinado autor:

`git log {{[-n|--max-count]}} {{número}} --author "{{autor}}"`

- Muestra las confirmaciones entre dos fechas (yyyy-mm-dd):

`git log --before "{{2017-01-29}}" --after "{{2017-01-17}}"`
