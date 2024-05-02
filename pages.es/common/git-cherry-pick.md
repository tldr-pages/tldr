# git cherry-pick

> Aplica los cambios introducidos por confirmaciones existentes a la rama actual.
> Para aplicar cambios a otra rama, primero utiliza `git checkout` para cambiar a la rama deseada.
> Más información: <https://git-scm.com/docs/git-cherry-pick>.

- Aplica una confirmación a la rama actual:

`git cherry-pick {{confirmación}}`

- Aplica un rango de confirmaciones de la rama actual (vea también `git rebase --onto`):

`git cherry-pick {{confirmación_inicial}}~..{{confirmación_final}}`

- Aplica múltiples confirmaciones no secuenciales a la rama actual:

`git cherry-pick {{confirmación_1 confirmación_2 ...}}`

- Añade los cambios de una confirmación al directorio de trabajo, sin crear una confirmación:

`git cherry-pick --no-commit {{confirmación}}`
