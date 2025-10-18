# make

> Ejecutor de tareas para objetivos descritos en Makefile.
> Se utiliza principalmente para controlar la compilación de un ejecutable a partir del código fuente.
> Más información: <https://www.gnu.org/software/make/manual/make.html>.

- Llama al primer objetivo especificado en el Makefile (normalmente llamado "all"):

`make`

- Llama a un objetivo específico:

`make {{objetivo}}`

- Llama a un objetivo específico, ejecutando 4 trabajos a la vez en paralelo:

`make {{[-j|--jobs]}} 4 {{objetivo}}`

- Utiliza un Makefile específico:

`make {{[-f|--file]}} {{ruta/al/archivo}}`

- Ejecuta make desde otro directorio:

`make {{[-C|--directory]}} {{ruta/al/directorio}}`

- Fuerza la creación de un objetivo, incluso si los archivos de origen no se han modificado:

`make {{[-B|--siempre-make]}} {{objetivo}}`

- Anula una variable definida en el Makefile:

`make {{objetivo}} {{variable}}={{nuevo_valor}}`

- Anula variables definidas en el Makefile por el entorno:

`make {{[-e|--environment-overrides]}} {{objetivo}}`
