# bash

> Bourne-Again SHell, un intérprete de línea de comandos compatible con `sh`.
> Vea también: `zsh`; `histexpand`, para expansión de historial de comandos.
> Más información: <https://www.gnu.org/software/bash/>.

- Inicia un intérprete de comandos interactivo:

`bash`

- Inicia el intérprete sin leer archivos de configuración:

`bash --norc`

- Ejecuta un comando:

`bash -c "{{comando}}"`

- Ejecuta comandos desde un archivo:

`bash {{archivo.sh}}`

- Ejecuta comandos desde un archivo, mostrando todos los comando ejecutados en la terminal:

`bash -x {{archivo.sh}}`

- Ejecuta comandos desde un archivo, deteniéndose en el primer error:

`bash -e {{archivo.sh}}`

- Ejecuta comandos desde `stdin` (entrada estándar):

`{{echo "echo 'bash es ejecutado'"}} | bash`

- Inicia el intérprete [r]estringido:

`bash -r`
