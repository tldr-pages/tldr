# git log

> Muestra un historial de commits.
> Más información: <https://git-scm.com/docs/git-log>.

- Muestra la secuencia de commits que comienza desde el actual, en orden cronológico inverso:

`git log`

- Muestra el historial de un archivo o directorio específico e incluye las diferencias:

`git log -p {{ruta/al/archivo_o_directorio}}`

- Muestra solo la primera línea de cada mensaje de commit:

`git log --oneline`

- Muestra un resumen de los archivos, o archivo, cambiados en cada commit:

`git log --stat`

- Muestra un gráfico de los commits en la rama actual:

`git log --graph`

- Muestra un gráfico de todos los commits, etiquetas y ramas en todo el repositorio:

`git log --oneline --decorate --all --graph`

- Muestra solo los commits cuyo mensaje incluya una cadena concreta (no diferencia entre mayúsculas y minúsculas):

`git log -i --grep {{cadena_a_buscar}}`
