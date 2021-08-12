# git switch

> Comutați între ramurile Git. Necesită versiunea Git 2.23+.
> A se vedea, de asemenea, `git checkout`.
> Mai multe informaţii: <https://git-scm.com/docs/git-switch>

- Comutarea la o ramură existentă:

`git switch {{branch_name}}`

- Creați o nouă ramură și treceți la ea:

`git switch --create {{branch_name}}`

- Creați o nouă sucursală bazată pe un angajament existent și treceți la acesta:

`git switch --create {{branch_name}} {{commit}}`

- Treceți la ramura anterioară:

`git switch -`

- Treceți la o ramură și actualizați toate submodulele pentru a se potrivi:

`git switch --recurse-submodules {{branch_name}}`

- Treceți la o sucursală și îmbinați automat ramura curentă și orice modificări neangajate în ea:

`git switch --merge {{branch_name}}`
