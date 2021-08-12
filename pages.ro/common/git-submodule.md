# git submodule

> Inspectează, actualizează și gestionează submodulele.
> Mai multe informaţii: <https://git-scm.com/docs/git-submodule>

- Instalați submodulele specificate ale unui depozit:

`git submodule update --init --recursive`

- Adăugați un depozit Git ca submodul:

`git submodule add {{repository_url}}`

- Adăugați un depozit Git ca submodul în directorul specificat:

`git submodule add {{repository_url}} {{path/to/directory}}`

- Actualizați fiecare submodul la cele mai recente angajamente:

`git submodule foreach git pull`
