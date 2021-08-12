# git flow

> O colecție de extensii Git pentru a oferi operațiuni de depozit la nivel înalt.
> Mai multe informaţii: <https://github.com/nvie/gitflow>

- Inițializați-l în interiorul unui depozit Git existent:

`git flow init`

- Începeți să dezvoltați pe o ramură caracteristică bazată pe `dezvoltare':

`git flow feature start {{feature}}`

- Finalizarea dezvoltării pe o ramură caracteristică, îmbinarea acesteia în ramura `dezvoltare și ștergerea acesteia:

`git flow feature finish {{feature}}`

- Publicați o caracteristică pe serverul de la distanță:

`git flow feature publish {{feature}}`

- Obțineți o caracteristică publicată de un alt utilizator:

`git flow feature pull origin {{feature}}`
