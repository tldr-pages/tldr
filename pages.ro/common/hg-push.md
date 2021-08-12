# hg push

> Apăsați modificările din depozitul local la o destinație specificată.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#push>

- Împingeți modificările la calea de la distanță „implicită”:

`hg push`

- Împingeți modificările la un depozit de la distanță specificat:

`hg push {{path/to/destination_repository}}`

- Împingeți o nouă ramură dacă nu există (dezactivată în mod implicit):

`hg push --new-branch`

- Specificați un anumit set de modificări de revizuire pentru a împinge:

`hg push --rev {{revision}}`

- Specificați o ramură specifică pentru a împinge:

`hg push --branch {{branch}}`

- Specificați un anumit marcaj pentru a împinge:

`hg push --bookmark {{bookmark}}`
