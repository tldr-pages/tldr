# ed

> El editor de texto original de Unix.
> Vea también: `awk`, `sed`.
> Más información: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia una sesión de edición interactiva con un documento vacío:

`ed`

- Inicia una sesión de edición interactiva con un documento vacío y un prompt específico:

`ed {{[-p|--prompt]}} '{{> }}'`

- Inicia una sesión de edición interactiva con errores de usuario:

`ed {{[-v|--verbose]}}`

- Inicia una sesión de edición interactiva con un documento vacío y sin diagnósticos, recuento de bytes ni indicaciones '!':

`ed {{[-q|--quiet]}} {{[-s|--script]}}`

- Inicia una sesión de edición interactiva sin cambio de estado de salida cuando falla el comando:

`ed {{[-l|--loose-exit-status]}}`

- Edita un archivo específico (muestra el recuento de bytes del archivo cargado):

`ed {{ruta/al/archivo}}`

- Reemplaza una cadena con un reemplazo específico para todas las líneas:

`,s/{{regex}}/{{replacement}}/g<Enter>`

- Sale de `ed`:

`q<Enter>`
