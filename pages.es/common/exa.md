# exa

> Un reemplazo moderno para `ls` (Lista el contenido de los directorios).
> Más información: <https://github.com/ogham/exa#command-line-options>.

- Lista los archivos uno por línea:

`exa {{[-1|--oneline]}}`

- Lista todos los archivos, incluidos los ocultos:

`exa {{[-a|--all]}}`

- Lista en formato largo (permisos, propiedad, tamaño y fecha de modificación) de todos los archivos:

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Lista los archivos con el más grande en la parte superior:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Muestra un árbol de archivos, con tres niveles de profundidad:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Lista archivos ordenados por fecha de modificación (los más antiguos primero):

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Muestra los archivos con sus encabezados, íconos y estados Git:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- No muestra los archivos mencionados en `.gitignore`:

`exa --git-ignore`
