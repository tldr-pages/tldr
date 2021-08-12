# git bundle

> Pachet obiecte și referințe într-o arhivă.
> Mai multe informaţii: <https://git-scm.com/docs/git-bundle>

- Creați un fișier pachet care conține toate obiectele și referințele unei anumite ramuri:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Creați un fișier pachet cu toate ramurile:

`git bundle create {{path/to/file.bundle}} --all`

- Creați un fișier pachet cu ultimele 5 angajări ale sucursalei curente:

`git bundle create {{path/to/file.bundle}} -{{5}} {{HEAD}}`

- Creați un fișier pachet de cele mai recente 7 zile:

`git bundle create {{path/to/file.bundle}} --since={{7.days}} {{HEAD}}`

- Verificați dacă un fișier pachet este valid și poate fi aplicat la depozitul curent:

`git bundle verify {{path/to/file.bundle}}`

- Imprimați la ieșirea standard lista de referințe conținute într-un pachet:

`git bundle unbundle {{path/to/file.bundle}}`

- Degrupați o ramură specifică dintr-un fișier pachet în depozitul curent:

`git pull {{path/to/file.bundle}} {{branch_name}}`
