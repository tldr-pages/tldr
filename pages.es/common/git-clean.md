# git clean

> Elimina archivos sin rastrear del árbol de trabajo.
> Más información: <https://git-scm.com/docs/git-clean>.

- Elimina archivos que no son rastreados por Git:

`git clean`

- Elimina interactivamente archivos que no son rastreados por Git:

`git clean {{--interactive|-i}}`

- Muestra que archivos serían borrados sin llegar a borrarlos:

`git clean --dry-run`

- Elimina forzosamente los archivos que no son rastreados por Git:

`git clean {{--force|-f}}`

- Elimina forzosamente los directorios que no son rastreados por Git:

`git clean {{--force|-f}} -d`

- Elimina archivos sin rastrear, incluyendo los archivos ignorados en `.gitignore` y los excluidos en `.git/info/exclude`:

`git clean -x`
