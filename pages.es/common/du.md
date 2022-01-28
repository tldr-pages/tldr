# du

> Uso de disco: estima y resume el uso de espacio en disco de archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/du>.

- Lista los tamaños de un directorio y sus subdirectorios en las unidades dadas (B/KiB/MiB):

`du -{{b|k|m}} {{ruta/al/directorio}}`

- Lista los tamaños de un directorio y sus subdirectorios en formato legible para humanos (es decir, seleccionando automáticamente las unidades apropiadas para cada tamaño):

`du -h {{ruta/al/directorio}}`

- Muestra el tamaño de un solo directorio en formato legible para humanos:

`du -sh {{ruta/al/directorio}}`

- Lista los tamaños legibles para humanos de un directorio y de todos los archivos y directorios dentro del mismo:

`du -ah {{ruta/al/directorio}}`

- Lista los tamaños legibles para humanos de un directorio y sus subdirectorios hasta N niveles de profundidad:

`du -h --max-depth=N {{ruta/al/directorio}}`

- Lista el tamaño legible para humanos de todos los archivos `.jpg` en subdirectorios del directorio actual y muestra un total al final:

`du -ch {{*/*.jpg}}`
