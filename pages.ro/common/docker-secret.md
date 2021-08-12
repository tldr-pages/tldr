# docker secret

> Gestionați secretele roi Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/secret/>

- Creați un nou secret de la stdin:

`{{command}} | docker secret create {{secret_name}} -`

- Creați un nou secret dintr-un fișier:

`docker secret create {{secret_name}} {{path/to/file}}`

- Listează toate secretele:

`docker secret ls`

- Afișați informații detaliate cu privire la unul sau mai multe secrete într-un format prietenos uman:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Eliminați unul sau mai multe secrete:

`docker secret rm {{secret_name1 secret_name2 ...}}`
