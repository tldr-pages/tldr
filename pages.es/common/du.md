# du

> Uso del disco: estima y resume el uso del espacio de archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Lista los tamaños de un directorio y sus subdirectorios, en la unidad dada (B/KiB/MiB):

`du -{{b|k|m}} {{ruta/al/directorio}}`

- Lista los tamaños de un directorio y sus subdirectorios, de forma legible (es decir, seleccionando automáticamente la unidad adecuada para cada tamaño):

`du {{[-h|--human-readable]}} {{ruta/al/directorio}}`

- Muestra el tamaño de un único directorio, en unidades legibles:

`du {{[-sh|--summarize --human-readable]}} {{ruta/al/directorio}}`

- Lista los tamaños legibles de un directorio y de todos los archivos y directorios que contiene:

`du -ah {{ruta/al/directorio}}`

- Lista los tamaños legibles de un directorio y sus subdirectorios, hasta N niveles de profundidad:

`du {{[-h|--human-readable]}} --max-depth=N {{ruta/al/directorio}}`

- Lista el tamaño legible de todos los archivos `.jpg` en los subdirectorios del directorio actual y muestra un total acumulado al final:

`du {{[-ch|--total --human-readable]}} {{*/*.jpg}}`

- Lista todos los archivos y directorios (incluidos los ocultos) por encima de un determinado tamaño (útil para investigar qué está ocupando realmente el espacio):

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`
