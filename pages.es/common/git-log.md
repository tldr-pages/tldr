# git log

> Muestra un historial de commits.
> Más información: <https://git-scm.com/docs/git-log>.

- Muestra la secuencia de commits comenzando desde el actual, en orden cronológico inverso, del respositorio de Git en el directorio de trabajo actual:

`git log`

- Muestra el historial de un archivo o directorio específico, incluyendo las diferencias:

`git log -p {{ruta/al/archivo_o_directorio}}`

- Muestra un resumen de los archivos, o archivo, cambiados en cada commit:

`git log --stat`

- Muestra un gráfico de los commits en la rama actual, utilizando solo la primer línea del mensaje de cada uno:

`git log --oneline --graph`

- Muestra un gráfico de todos los commits, etiquetas y ramas en todo el repositorio:

`git log --oneline --decorate --all --graph`

- Muestra solo los commits cuyo mensaje incluye una cadena dada (no diferencia entre mayúsculas y minúsculas):

`git log -i --grep {{cadena_a_buscar}}`

- Muestra los últimos N commits de cierto autor:

`git log -n {{numero}} --author={{autor}}`

- Muestra los commits entre dos fechas (yyyy-mm-dd):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
