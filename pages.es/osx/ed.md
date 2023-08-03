# ed

> El editor de texto original de Unix.
> Ver también: `awk`, `sed`.
> Más información: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia una sesión de edición interactiva con un documento vacío:

`ed`

- Inicia una sesión de editor interactivo con un documento vacío y un [p]rompt específico:

`ed -p '> '`

- Inicia una sesión de editor interactivo con un documento vacío y sin diagnósticos, recuento de bytes y prompt '!':

`ed -s`

- Edita un archivo específico (muestra el recuento de bytes del archivo cargado):

`ed {{ruta/al/archivo}}`

- Reemplaza una cadena con un reemplazo específico para todas las líneas:

`,s/{{expresión_regular}}/{{reemplazo}}/g`
