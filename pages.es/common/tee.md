# tee

> Lee desde la entrada estándar (`stdin`) y escribe a la salida estándar (`stdout`) y a archivos (o comandos).
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Copia la entrada estándar (`stdin`) a cada archivo, y también a la salida estándar (`stdout`):

`echo "ejemplo" | tee {{ruta/al/archivo}}`

- Anexa a los archivos específicos, sin sobreescribir:

`echo "ejemplo" | tee {{[-a|--append]}} {{ruta/al/archivo}}`

- Imprime la entrada estándar a la terminal, y también lo reenvía a otro programa para posterior procesamiento:

`echo "ejemplo" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Crea un directorio llamado "ejemplo", cuenta el número de caracteres en "ejemplo" y escribe "ejemplo" a la terminal:

`echo "ejemplo" | tee >(xargs mkdir) >(wc -c)`
