# mktemp

> Crea un archivo o directorio temporal.
> Más información: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Crea un archivo temporal vacío e imprime su ruta absoluta:

`mktemp`

- Usa un directorio personalizado (por defecto la salida de `getconf DARWIN_USER_TEMP_DIR`, o `/tmp`):

`mktemp --tmpdir={{/ruta/a/tempdir}}`

- Usa una plantilla de ruta personalizada (las `X` se sustituyen por caracteres alfanuméricos aleatorios):

`mktemp {{/tmp/ejemplo.XXXXXXXX}}`

- Usa un prefijo de nombre de archivo personalizado:

`mktemp -t {{ejemplo}}`

- Crea un directorio temporal vacío e imprime su ruta absoluta:

`mktemp --directory`
