# dircolors

> Comandos de salida para establecer la variable de entorno LS_COLOR y el estilo `ls`, `dir`, etc.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Comandos de salida para establecer LS_COLOR usando los colores por defecto:

`dircolors`

- Muestra cada tipo de fichero con el color con el que aparecerían en `ls`:

`dircolors --print-ls-colors`

- Comandos de salida para establecer LS_COLOR utilizando los colores de un archivo:

`dircolors {{ruta/al/archivo}}`

- Comandos de salida para el intérprete de comandos Bourne:

`dircolors {{[-b|--bourne-shell]}}`

- Comandos de salida para el intérprete de comandos C:

`dircolors {{[-c|--c-shell]}}`

- Visualiza los colores predeterminados según los tipos de archivo y extensiones:

`dircolors {{[-p|--print-database]}}`
