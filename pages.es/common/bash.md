# bash

> Bourne-Again SHell.
> Intérprete de línea de comandos compatible con `sh`.
> Más información: <https://gnu.org/software/bash/>.

- Inicia un intérprete de comandos interactivo:

`bash`

- Ejecuta un comando:

`bash -c "{{comando}}"`

- Ejecuta comandos desde un archivo:

`bash {{archivo.sh}}`

- Ejecuta comandos desde un archivo, mostrando todos los comando ejecutados en la terminal:

`bash -x {{archivo.sh}}`

- Ejecuta comandos desde un archivo, deteniéndose en el primer error:

`bash -e {{archivo.sh}}`

- Ejecuta comandos desde `stdin` (entrada estándar):

`bash -s`

- Imprime la información de la versión de bash (use `echo $BASH_VERSION` para ver sólo la versión sin la información sobre la licencia):

`bash --version`
