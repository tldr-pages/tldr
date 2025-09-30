# diff

> Compara archivos y directorios.
> Más información: <https://manned.org/diff>.

- Compara archivos (lista los cambios para convertir `archivo_viejo` en `archivo_nuevo`):

`diff {{archivo_viejo}} {{archivo_nuevo}}`

- Compara archivos, ignorando los espacios en blanco:

`diff {{[-w|--ignore-all-space]}} {{archivo_viejo}} {{archivo_nuevo}}`

- Compara archivos, mostrando las diferencias lado a lado:

`diff {{[-y|--side-by-side]}} {{archivo_viejo}} {{archivo_nuevo}}`

- Compara archivos, mostrando las diferencias en formato unificado (como el que usa `git diff`):

`diff {{[-u|--unified]}} {{archivo_viejo}} {{archivo_nuevo}}`

- Compara directorios de forma recursiva (muestra los nombres de los archivos/directorios que difieran y los cambios realizados en los archivos):

`diff {{[-r|--recursive]}} {{directorio_viejo}} {{directorio_nuevo}}`

- Compara directorios, mostrando solo los nombres de los archivos que difieren:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{directorio_viejo}} {{directorio_nuevo}}`

- Crea un archivo de revisión para Git a partir de las diferencias entre dos archivos de texto, tratando los archivos inexistentes como vacíos:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{archivo_viejo}} {{archivo_nuevo}} > {{diff.patch}}`

- Compara archivos, mostrando la salida en color y se esfuerza por encontrar el conjunto más pequeño de cambios:

`diff {{[-d|--minimal]}} --color=always {{archivo_viejo}} {{archivo_nuevo}}`
