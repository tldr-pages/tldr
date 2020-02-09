# git check-ignore

> Analiza y depura los archivos que git debe ignorar / excluir (.gitignore).
> Más información: <https://git-scm.com/docs/git-check-ignore>.

- Comprueba si un archivo o directorio es ignorado:

`git check-ignore {{ruta/del/archivo_o_directorio}}`

- Comprueba si varios archivos o directorios son ignorados:

`git check-ignore {{ruta/del/archivo}} {{ruta/del/directorio}}`

- Usa nombres de rutas, uno por línea, a partir de la entrada estandar (`stdin`):

`git check-ignore --stdin < {{ruta/del/archivo_lista}}`

- No comprueba el índice (se utiliza para depurar por qué las rutas fueron rastreadas y no ignoradas):

`git check-ignore --no-index {{ruta/de_los/archivos_o_directorios}}`

- Incluye detalles sobre el patrón de coincidencia para cada ruta:

`git check-ignore --verbose {{ruta/de_los/archivos_o_directorios}}`
