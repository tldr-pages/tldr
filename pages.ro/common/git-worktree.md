# git worktree

> Gestionați mai mulți arbori de lucru atașați la același depozit.
> Mai multe informaţii: <https://git-scm.com/docs/git-worktree>

- Creați un nou director cu ramura specificată verificată în el:

`git worktree add {{path/to/directory}} {{branch}}`

- Creați un nou director cu o nouă ramură verificată în el:

`git worktree add {{path/to/directory}} -b {{new_branch}}`

- Listați toate directoarele de lucru atașate la acest depozit:

`git worktree list`

- Eliminați un arbore de lucru (după ștergerea directorului arborelui de lucru):

`git worktree prune`
