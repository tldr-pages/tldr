# exa

> Un reemplazo moderno para `ls` (Lista el contenido de los directorios).
> Más información: <https://github.com/ogham/exa#command-line-options>.

- Lista archivos uno por línea:

`exa {{[-1|--oneline]}}`

- Lista todos los archivos, incluidos los ocultos:

`exa {{[-a|--all]}}`

- Lista en formato largo (permisos, propiedad, tamaño y fecha de modificación) de todos los archivos:

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Muestra los archivos con el más grande al principio:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Muestra un árbol de archivos de tres niveles de profundidad:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Lista los archivos ordenados por fecha de modificación (los más antiguos primero):

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Lista de archivos con sus cabeceras, iconos y estados Git:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- No lista los archivos mencionados en `.gitignore`:

`exa --git-ignore`
