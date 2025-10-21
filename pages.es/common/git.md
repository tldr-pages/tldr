# git

> Sistema de control de versiones distribuido.
> Algunos subcomandos como `commit`, `add`, `branch`, `switch`, `push`, etc. tienen su propia documentación de uso.
> Más información: <https://git-scm.com/docs/git>.

- Crea un repositorio Git vacío:

`git init`

- Clona un repositorio Git remoto desde Internet:

`git clone {{https://example.com/repo.git}}`

- Muestra el estado del repositorio local:

`git status`

- Preparar todos los cambios para un commit:

`git add {{[-A|--all]}}`

- Confirma los cambios en el historial de versiones:

`git commit {{[-m|--message]}} {{texto_del_mensaje}}`

- Envía los commits locales a un repositorio remoto:

`git push`

- Obtener los cambios realizados en un remoto:

`git pull`

- Restablecer todo al estado del último commit:

`git reset --hard; git clean {{[-f|--force]}}`
