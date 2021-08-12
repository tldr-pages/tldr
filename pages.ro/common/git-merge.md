# git merge

> Îmbinaţi ramurile.
> Mai multe informaţii: <https://git-scm.com/docs/git-merge>

- Îmbinați o ramură în sucursala dvs. curentă:

`git merge {{branch_name}}`

- Editați mesajul de îmbinare:

`git merge -e {{branch_name}}`

- Îmbinați o ramură și creați un angajament de îmbinare:

`git merge --no-ff {{branch_name}}`

- Abandonați o fuziune în caz de conflicte:

`git merge --abort`
