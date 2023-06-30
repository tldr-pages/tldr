# git cherry-pick

> Aplica los cambios introducidos por commits existentes a la rama actual.
> Para aplicar cambios a otra rama, primero utiliza `git checkout` para cambiar a la rama deseada.
> Más información: <https://git-scm.com/docs/git-cherry-pick>.

- Aplica un commit a la rama actual:

`git cherry-pick {{commit}}`

- Aplica un rango de commits de la rama actual (véase también `git rebase --onto`):

`git cherry-pick {{commit_inicial}}~..{{commit_final}}`

- Aplica múltiples commits no secuenciales a la rama actual:

`git cherry-pick {{commit_1}} {{commit_2}}`

- Añade los cambios de un commit al directorio de trabajo, sin crear un commit:

`git cherry-pick --no-commit {{commit}}`
