# git branch

> Comando principal de Git para trabajar con ramas.
> Más información: <https://git-scm.com/docs/git-branch>.

- Lista todas las ramas (locales y remotas; la rama actual se resalta con `*`):

`git branch --all`

- Lista las ramas que incluyen una confirmación específica en su historial:

`git branch --all --contains {{hash_de_la_confirmación}}`

- Muestra el nombre de la rama actual:

`git branch --show-current`

- Crea una nueva rama basada en la confirmación actual:

`git branch {{nombre_rama}}`

- Crea una nueva rama basada en una confirmación específica:

`git branch {{nombre_de_rama}} {{hash_de_la_confirmación}}`

- Renombra una rama (para ello no debes tenerla controlada):

`git branch -m {{nombre_de_rama_antigua}} {{nuevo_nombre_rama}}`

- Elimina una rama local (no debes tenerla controlada para hacerlo):

`git branch -d {{nombre_de_rama}}`

- Elimina una rama remota:

`git push {{nombre_remoto}} --delete {{nombre_de_rama_remota}}`
