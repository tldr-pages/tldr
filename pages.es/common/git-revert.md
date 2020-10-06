# git revert

> Crea nuevos commits que revierten el efecton de los anteriores.
> Más información: <https://git-scm.com/docs/git-revert>.

- Revierte el commit más reciente:

`git revert {{@}}`

- Revierte el quinto último commit:

`git revert HEAD~{{4}}`

- Revierte múltiples commits:

`git revert {{master~5..master~2}}`

- No crea nuevos commits, solo cambia el árbol de trabajo:

`git revert -n {{0c01a9..9a1743}}`
