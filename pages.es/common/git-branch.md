# git branch

> Comando Git principal para trabajar con ramas.
> Más información: <https://git-scm.com/docs/git-branch>.

- Muestra las ramas locales. La rama actual está resaltada por `*`:

`git branch`

- Muestra todas las ramas (locales y remotas):

`git branch -a`

- Muestra el nombre de la rama actual:

`git branch --show-current`

- Crea una nueva rama basada en el commit actual:

`git branch {{nombre_de_la_rama}}`

- Crea una nueva rama basada en un commit específico:

`git branch {{nombre_de_rama}} {{hash_del_commit}}`

- Renombra una rama (no debe haber sido fusionada para hacer esto):

`git branch -m {{antiguo_nombre_de_la_rama}} {{nuevo_nombre_de_la_rama}}`

- Borra una rama local (no debe haber sido fusionada para hacer esto):

`git branch -d {{nombre_de_la_rama}}`

- Borra una rama remota:

`git push {{nombre_remoto}} --delete {{nombre_de_la_rama_remota}}`
