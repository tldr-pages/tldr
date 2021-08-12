# dolt branch

> Gestionați ramurile Dolt.
> Mai multe informaţii: <https://github.com/dolthub/dolt>

- Lista sucursalelor locale (sucursala curentă este evidențiată prin `*`):

`dolt branch`

- Listați toate sucursalele locale și îndepărtate:

`dolt branch --all`

- Creați o nouă sucursală bazată pe sucursala curentă:

`dolt branch {{branch_name}}`

- Creați o nouă sucursală cu angajamentul specificat ca cel mai recent:

`dolt branch {{branch_name}} {{commit}}`

- Redenumiți o ramură:

`dolt branch --move {{branch_name1}} {{branch_name2}}`

- Duplicarea unei sucursale:

`dolt branch --copy {{branch_name1}} {{branch_name2}}`

- Şterge o ramură:

`dolt branch --delete {{branch_name}}`

- Afișează numele sucursalei curente:

`dolt branch --show-current`
