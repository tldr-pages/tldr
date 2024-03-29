# git push

> Envía (*push*) los commits al repositorio remoto.
> Más información: <https://git-scm.com/docs/git-push>.

- Envía los cambios locales en la rama actual a la misma rama en el remoto:

`git push`

- Envía los cambios locales de una rama específica a la misma rama en el remoto:

`git push {{nombre_remoto}} {{rama_local}}`

- Publica la rama actual en el repositorio remoto y establece el nombre remoto de la rama:

`git push -u {{nombre_remoto}} {{rama_remota}}`

- Envía los cambios locales de una rama específica a una rama específica en el remoto:

`git push {{nombre_remoto}} {{rama_local}}:{{rama_remota}}`

- Envía los cambios de todas las ramas locales a sus respectivas ramas en el repositorio remoto:

`git push --all {{nombre_remoto}}`

- Elimina una rama en el repositorio remoto:

`git push {{nombre_remoto}} --delete {{rama_remota}}`

- Elimina las ramas remotas que no están en el repositorio local:

`git push --prune {{nombre_remoto}}`

- Publica las etiquetas que aún no están en el repositorio remoto:

`git push --tags`
