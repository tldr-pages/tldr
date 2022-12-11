# touch

> Cambia el tiempo de accesso y modificación de un archivo (atime, mtime).
> Más información: <https://www.gnu.org/software/coreutils/touch>.

- Crea un archivo nuevo o cambia los tiempos de archivos existentes al tiempo actual:

`touch {{archivo}}`

- Establece los tiempos de un archivo a un día y hora específicos:

`touch -t {{YYYYMMDDHHMM.SS}} {{archivo}}`

- Usa los tiempos de un archivo para establecer los tiempos en otro archivo:

`touch -r {{archivo}} {{archivo2}}`
