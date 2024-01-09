# git merge

> Fusiona ramas.
> Más información: <https://git-scm.com/docs/git-merge>.

- Fusiona una rama con la rama actual:

`git merge {{nombre_de_la_rama}}`

- Edita el mensaje de fusión:

`git merge -e {{nombre_de_la_rama}}`

- Fusiona una rama y crea una confirmación para la fusión:

`git merge --no-ff {{nombre_de_la_rama}}`

- Cancela una fusión en caso de conflictos:

`git merge --abort`
