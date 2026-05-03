# eza

> Versión moderna y actualizada de `ls`, basada en `exa`.
> Más información: <https://github.com/eza-community/eza>.

- Muestra los archivos uno por línea:

`eza {{[-1|--oneline]}}`

- Muestra todos los archivos, incluidos los ocultos:

`eza {{[-a|--all]}}`

- Muestra una lista detallada (permisos, propietario, tamaño y fecha de modificación) de todos los archivos:

`eza {{[-al|--all --long]}}`

- Muestra los archivos ordenados de mayor a menor:

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Muestra un árbol de archivos con tres niveles de profundidad:

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- Lista los archivos ordenados por fecha de modificación (los más antiguos primero):

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Muestra los archivos con sus encabezados, iconos y estados de Git:

`eza {{[-lh|--long --header]}} --icons --git`

- No muestra los archivos mencionados en `.gitignore`:

`eza --git-ignore`
