# ed

> El editor de texto original de Unix.
> Vea también: `awk`, `sed`.
> Más información: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia una sesión de editor interactivo con un documento vacío:

`ed`

- Inicia una sesión de editor interactivo con un documento vacío y un prompt específico:

`ed {{[-p|--prompt]}} '{{> }}'`

- Inicia una sesión de editor interactivo con errores amigables:

`ed {{[-v|--verbose]}}`

- Inicia una sesión de editor interactivo con un documento vacío y sin diagnósticos, conteos de bytes y prompt de '!':

`ed {{[-q|--quiet]}}`

- Inicia una sesión de editor interactivo sin cambio de estado de salida cuando un comando falla:

`ed {{[-l|--loose-exit-status]}}`

- Edita un archivo específico (esto muestra el conteo de bytes del archivo cargado):

`ed {{ruta/al/archivo}}`

- Reemplaza una cadena con un reemplazo específico en todas las líneas:

`,s/{{expresión_regular}}/{{reemplazo}}/g`
