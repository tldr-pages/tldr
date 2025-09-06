# touch

> Crea archivos y establece los tiempos de acceso y modificación.
> Más información: <https://manned.org/touch>.

- Crea los archivos especificados:

`touch {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Establece los tiempos de [a]cceso o [m]odificación al momento actual y no [c]rea un archivo si este no existe:

`touch {{[-c|--no-create]}} -{{a|m}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Establece los [t]iempos de un archivo a un valor específico y no [c]rea el archivo si no existe:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Usa los tiempos de un archivo de [r]eferencia para establecer los tiempos en otro archivo y no [c]rea el archivo si no existe:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{ruta/al/archivo/de/referencia}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
