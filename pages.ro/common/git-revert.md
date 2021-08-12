# git revert

> Creați angajări noi care inversează efectul celor anterioare.
> Mai multe informaţii: <https://git-scm.com/docs/git-revert>

- Reveniți cel mai recent angajament:

`git revert {{@}}`

- Reveniți a 5-a ultima comite:

`git revert HEAD~{{4}}`

- Reveniți mai multe angajamente:

`git revert {{branch_name~5..branch_name~2}}`

- Nu creați noi angajări, doar schimbați arborele de lucru:

`git revert -n {{0c01a9..9a1743}}`
