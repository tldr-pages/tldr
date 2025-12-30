# git clone

> Clonează un repository existent.
> Mai multe informații: <https://git-scm.com/docs/git-clone>.

- Clonează un repository la distanță existent:

`git clone {{url_repository_la_distanță}}`

- Clonează un repository la distanță împreună cu submodulele sale:

`git clone --recursive {{url_repository_la_distanță}}`

- Clonează un repository local:

`git clone -l {{cale/către/repository/local}}`

- Clonează în mod silențios:

`git clone -q {{url_depozit_la_distanță}}`

- Clonează un repository la distanță descărcând doar cele 10 commit-uri cele mai recente ale ramurii principale (util pentru a economisi timp):

`git clone --depth 10 {{url_depozit_la_distanță}}`
