# dolt checkout

> Verificați arborele de lucru sau tabelele într-o anumită ramură sau comite.
> Mai multe informaţii: <https://github.com/dolthub/dolt>

- Treceți la o ramură:

`dolt checkout {{branch_name}}`

- Reveniți modificările neetalate la un tabel:

`dolt checkout {{table}}`

- Creați o nouă ramură și treceți la ea:

`dolt checkout -b {{branch_name}}`

- Creați o nouă sucursală bazată pe un angajament specificat și comutați la acesta:

`dolt checkout -b {{branch_name}} {{commit}}`
