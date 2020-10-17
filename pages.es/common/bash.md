# bash

> Bourne-Again SHell.
> Intérprete de línea de comandos compatible con `sh`.
> Más información: <https://gnu.org/software/bash>.

- Iniciar *shell* interactiva:

`bash`

- Ejecutar un comando:

`bash -c "{{comando}}"`

- Ejecutar comandos desde un archivo:

`bash {{archivo.sh}}`

- Ejecutar comandos desde un archivo, registrando todos los comando ejecutados en la terminal:

`bash -x {{archivo.sh}}`

- Ejecutar comandos desde un archivo, deteniéndose en el primer error:

`bash -e {{archivo.sh}}`

- Ejecuta comandos desde `stdin` (entrada estándar):

`bash -s`

- Imprime la información de la versión de bash (usa `echo $BASH_VERSION` para ver solo la cadena de la versión):

`bash --version`
