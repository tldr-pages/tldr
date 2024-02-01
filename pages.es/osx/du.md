# du

> Uso del disco: estima y resume el uso del espacio de archivos y directorios.
> Más información: <https://keith.github.io/xcode-man-pages/du.1.html>.

- Lista los tamaños de un directorio y de cualquier subdirectorio, en la unidad dada (KiB/MiB/GiB):

`du -{{k|m|g}} {{ruta/al/directorio}}`

- Enumera los tamaños de un directorio y sus subdirectorios, de forma legible (es decir, seleccionando automáticamente la unidad adecuada para cada tamaño):

`du -h {{ruta/al/directorio}}`

- Muestra el tamaño de un único directorio, en unidades legibles para el ser humano:

`du -sh {{ruta/al/directorio}}`

- Muestra los tamaños legibles de un directorio y de todos los archivos y directorios que contiene:

`du -ah {{ruta/al/directorio}}`

- Lista los tamaños legibles de un directorio y sus subdirectorios, hasta N niveles de profundidad:

`du -h -d {{2}} {{ruta/al/directorio}}`

- Lista el tamaño legible de todos los archivos `.jpg` en los subdirectorios del directorio actual y muestra un total acumulado al final:

`du -ch {{*/*.jpg}}`
