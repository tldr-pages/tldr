# git branch

> Comanda principală Git pentru lucrul cu ramuri.
> Mai multe informații: <https://git-scm.com/docs/git-branch>.

- Listează toate ramurile (locale și la distanță; ramura curentă este evidențiată cu un `*`):

`git branch {{[-a|--all]}}`

- Listează care ramuri includ un commit Git specific în istoricul lor:

`git branch {{[-a|--all]}} --contains {{hash_commit}}`

- Afișează numele ramurii curente:

`git branch --show-current`

- Creează o ramură nouă pornind de la commit-ul curent:

`git branch {{nume_ramură}}`

- Creează o ramură nouă pornind de la commit-ul specificat:

`git branch {{nume_ramură}} {{hash_commit}}`

- Redenumește o ramură (trebuie să comuti pe o altă ramură înainte de a face asta):

`git branch {{[-m|--move]}} {{nume_ramură_veche}} {{nume_ramură_nouă}}`

- Șterge o ramură locală (trebuie să comuti pe o altă ramură înainte de a face asta):

`git branch {{[-d|--delete]}} {{nume_ramură}}`

- Șterge o ramură la distanță:

`git push {{nume_la_distanță}} {{[-d|--delete]}} {{nume_ramură_la_distanță}}`
