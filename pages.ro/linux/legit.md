# legit

> Interfață complementară de linie de comandă pentru Git.
> Mai multe informaţii: <https://frostming.github.io/legit>

- Treceți la o ramură specificată, ascunzând și restabilind modificările neetajate:

`git switch {{target_branch}}`

- Sincronizați ramura curentă, fuzionând automat sau rebasing, și stashing și dezstashing:

`git sync`

- Publicați o ramură specificată pe serverul de la distanță:

`git publish {{branch_name}}`

- Eliminați o ramură de pe serverul de la distanță:

`git unpublish {{branch_name}}`

- Lista tuturor sucursalelor și statutul lor de publicare:

`git branches {{glob_pattern}}`

- Eliminați ultima comitere din istoric:

`git undo {{--hard}}`
