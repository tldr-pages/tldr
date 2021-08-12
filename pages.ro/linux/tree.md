# tree

> Afișați conținutul directorului curent ca arbore.
> Mai multe informaţii: <http://mama.indstate.edu/users/ice/tree/>

- Imprimați fișiere și directoare până la nivelurile de adâncime „num” (unde 1 înseamnă directorul curent):

`tree -L {{num}}`

- Doar tipăriţi directoare:

`tree -d`

- Imprimați fișiere ascunse prea cu colorarea pe:

`tree -a -C`

- Imprimați arborele fără linii de indentare, afișând în schimb calea completă (utilizați `-N` pentru a nu scăpa de caracterele neimprimabile):

`tree -i -f`

- Imprimați dimensiunea fiecărui fișier și dimensiunea cumulativă a fiecărui director, în format care poate fi citit de om:

`tree -s -h --du`

- Imprimați fișiere în ierarhia arborelui, utilizând un model wildcard (glob) și tăierea directoarelor care nu conțin fișiere potrivite:

`tree -P '{{*.txt}}' --prune`

- Imprimați directoare în ierarhia arborelui, utilizând modelul wildcard (glob) și tăierea directoarelor care nu sunt strămoșii celui căutat:

`tree -P {{directory_name}} --matchdirs --prune`

- Imprimați arborele ignorând directoarele date:

`tree -I '{{directory_name1|directory_name2}}'`
