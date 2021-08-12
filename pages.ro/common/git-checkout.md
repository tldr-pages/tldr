# git checkout

> Checkout o ramură sau căi către arborele de lucru.
> Mai multe informaţii: <https://git-scm.com/docs/git-checkout>

- Creați și treceți la o nouă ramură:

`git checkout -b {{branch_name}}`

- Creați și comutați la o nouă ramură bazată pe o referință specifică (ramură, telecomandă/ramură, tag-ul sunt exemple de referințe valide):

`git checkout -b {{branch_name}} {{reference}}`

- Comutarea la o sucursală locală existentă:

`git checkout {{branch_name}}`

- Treceți la ramura verificată anterior:

`git checkout -`

- Treceți la o ramură de la distanță existentă:

`git checkout --track {{remote_name}}/{{branch_name}}`

- Aruncați toate modificările neetapizate din directorul curent (consultați `git reset` pentru mai multe comenzi asemănătoare undo-like):

`git checkout .`

- Aruncați modificările neetalate într-un fișier dat:

`git checkout {{filename}}`

- Înlocuiți un fișier în directorul curent cu versiunea sa comis într-o anumită ramură:

`git checkout {{branch_name}} -- {{filename}}`
