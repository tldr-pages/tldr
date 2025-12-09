# diskutil partitionDisk

> Utilidad para gestionar particiones en discos y volúmenes.
> Parte de `diskutil`.
> APM solo es compatible con macOS, MBR está optimizado para DOS, mientras que GPT es compatible con la mayoría de los sistemas operativos modernos.
> Más información: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Reformatea un volumen usando el esquema de particionado APM/MBR/GPT, sin dejar particiones en su interior (esto borrará todos los datos del volumen):

`diskutil partitionDisk {{/dev/dispositivo_de_disco}} 0 {{APM|MBR|GPT}}`

- Reformatea un volumen, luego crea una única partición usando un sistema de archivos específico llenando todo el espacio libre:

`diskutil partitionDisk {{/dev/dispositivo_de_disco}} 1 {{APM|MBR|GPT}} {{partición_con_sistema_de_archivos}} {{nombre_de_partición}}`

- Reformatea un volumen, luego crea una única partición con un sistema de archivos y tamaño específico (ej. `16G` para 16GB o `50%` para llenar la mitad del tamaño total del volumen):

`diskutil partitionDisk {{/dev/dispositivo_de_disco}} 1 {{APM|MBR|GPT}} {{partición_con_sistema_de_archivos}} {{nombre_de_partición}} {{tamaño_de_partición}}`

- Reformatea un volumen y crea múltiples particiones:

`diskutil partitionDisk {{/dev/dispositivo_disco}} {{número_particiones}} {{APM|MBR|GPT}} {{partición_sistema_archivos1}} {{nombre_partición1}} {{tamaño_partición1}} {{partición_sistema_archivos2}} {{nombre_partición2}} {{tamaño_partición2}} ...`

- Lista todos los sistemas de ficheros soportados para particionar:

`diskutil listFilesystems`
