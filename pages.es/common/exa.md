# exa

> Un reemplazo moderno para `ls` (Lista el contenido de los directorios).
> Más información: <https://github.com/ogham/exa>.

- Lista archivos uno por línea:

`exa --oneline`

- Lista todos los archivos, incluidos los ocultos:

`exa --all`

- Lista en formato largo (permisos, propiedad, tamaño y fecha de modificación) de todos los archivos:

`exa --long --all`

- Muestra los archivos con el más grande al principio:

`exa --reverse --sort={{size}}`

- Muestra un árbol de archivos de tres niveles de profundidad:

`exa --long --tree --level={{3}}`

- Lista los archivos ordenados por fecha de modificación (los más antiguos primero):

`exa --long --sort={{modified}}`

- Lista de archivos con sus cabeceras, iconos y estados Git:

`exa --long --header --icons --git`

- No lista los archivos mencionados en `.gitignore`:

`exa --git-ignore`
