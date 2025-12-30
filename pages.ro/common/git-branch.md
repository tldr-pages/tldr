# git branch

> Comanda principală Git pentru lucrul cu ramuri.
> Mai multe informații: <https://git-scm.com/docs/git-branch>.

- Listează ramurile locale. Ramul curent este evidențiat cu un `*`:

`git branch`

- Listează toate ramurile (locale și la distanță):

`git branch {{[-a|--all]}}`

- Creează o ramură nouă pornind de la commit-ul curent:

`git branch {{nume_ramură}}`

- Creează o ramură nouă pornind de la commit-ul specificat:

`git branch {{nume_ramură}} {{hash_commit}}`

- Redenumește o ramură (nu se aplică pe ramul curent):

`git branch {{[-m|--move]}} {{nume_vechi}} {{nume_nou}}`

- Șterge o ramură locală (nu se aplică pe ramul curent):

`git branch {{[-d|--delete]}} {{nume_ramură}}`
