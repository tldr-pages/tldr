# git-grep

> Encuentra dentro de archivos en cualquier parte del historial del repositorio.
> Acepta una gran cantidad de opciones, de la misma manera que el comando `grep`.
> Más información: <https://git-scm.com/docs/git-grep>.

- Busca una cadena en los archivos rastreados:

`git grep {{cadena_a_buscar}}`

- Busca una cadena en archivos que coincidan con un patrón entre los archivos rastreados:

`git grep {{cadena_a_buscar}} -- {{patrón_de_archivos}}`

- Busca una cadena en los archivos rastreados, incluyendo submódulos:

`git grep --recurse-submodules {{cadena_a_buscar}}`

- Busca una cadena en un punto específico del historial:

`git grep {{cadena_a_buscar}} {{HEAD~2}}`

- Busca una cadena a través de todas las ramas:

`git grep {{cadena_a_buscar}} $(git rev-list --all)`
