# git branch

> Comanda principală Git pentru lucrul cu sucursalele.
> Mai multe informaţii: <https://git-scm.com/docs/git-branch>

- Lista sucursalelor locale. Sucursala curentă este evidențiată prin `*`:

`git branch`

- Listați toate sucursalele (locale și la distanță):

`git branch -a`

- Afișați numele sucursalei curente:

`git branch --show-current`

- Creați o nouă sucursală bazată pe angajamentul curent:

`git branch {{branch_name}}`

- Creați o nouă sucursală bazată pe un angajament specific:

`git branch {{branch_name}} {{commit_hash}}`

- Redenumiți o sucursală (nu trebuie să o verificați pentru a face acest lucru):

`git branch -m {{old_branch_name}} {{new_branch_name}}`

- Ștergeți o sucursală locală (nu trebuie să o verificați pentru a face acest lucru):

`git branch -d {{branch_name}}`

- Ștergeți o ramură la distanță:

`git push {{remote_name}} --delete {{remote_branch_name}}`
