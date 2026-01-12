# git clone

> Clonează un repository existent.
> Mai multe informații: <https://git-scm.com/docs/git-clone>.

- Clonează un repository existent într-un director nou (directorul implicit este numele repository-ului):

`git clone {{locație_repository_la_distanță}} {{cale/către/director}}`

- Clonează un repository existent împreună cu submodulele lui:

`git clone --recursive {{locație_repository_la_distanță}}`

- Clonează doar directorul `.git` al unui repository existent:

`git clone {{[-n|--no-checkout]}} {{locație_repository_la_distanță}}`

- Clonează un repository local:

`git clone {{[-l|--local]}} {{cale/către/repository_local}}`

- Clonează în mod silențios:

`git clone {{[-q|--quiet]}} {{locație_repository_la_distanță}}`

- Clonează un repository existent descărcând doar cele 10 commit-uri cele mai recente de pe ramura implicită (util pentru a economisi timp):

`git clone --depth 10 {{locație_repository_la_distanță}}`

- Clonează un repository existent descărcând doar o ramură specifică:

`git clone {{[-b|--branch]}} {{nume}} --single-branch {{locație_repository_la_distanță}}`

- Clonează un repository existent folosind o comandă SSH specifică:

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i cale/către/cheie_ssh_privata}}" {{locație_repository_la_distanță}}`
