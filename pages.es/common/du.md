# du

> Uso del disco: estima y resume el uso del espacio de archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/du>.

- Lista los tamaños de un directorio y sus subdirectorios, en la unidad dada (B/KiB/MiB):

`du -{{b|k|m}} {{ruta/al/directorio}}`

- Lista los tamaños de un directorio y sus subdirectorios, de forma legible (es decir, seleccionando automáticamente la unidad adecuada para cada tamaño):

`du -h {{ruta/al/directorio}}`

- Muestra el tamaño de un único directorio, en unidades legibles:

`du -sh {{ruta/al/directorio}}`

- Lista los tamaños legibles de un directorio y de todos los archivos y directorios que contiene:

`du -ah {{ruta/al/directorio}}`

- Lista los tamaños legibles de un directorio y sus subdirectorios, hasta N niveles de profundidad:

`du -h --max-depth=N {{ruta/al/directorio}}`

- Lista el tamaño legible de todos los archivos `.jpg` en los subdirectorios del directorio actual y muestra un total acumulado al final:

`du -ch {{*/*.jpg}}`

- Lista todos los archivos y directorios (incluidos los ocultos) por encima de un determinado tamaño (útil para investigar qué está ocupando realmente el espacio):

`du --all --human-readable --threshold {{1G|1024M|1048576K}} .[^.]* *`
