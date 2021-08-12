# docker-compose

> Rulați și gestionați aplicații multiple de andocare a containerelor.
> Mai multe informaţii: <https://docs.docker.com/compose/reference/overview/>

- Listează toate containerele care rulează:

`docker-compose ps`

- Creați și porniți toate containerele din fundal folosind un fișier `docker-compose.yml` din directorul curent:

`docker-compose up -d`

- Porniți toate containerele, reconstruiți dacă este necesar:

`docker-compose up --build`

- Porniți toate containerele folosind un fișier alternativ de compunere:

`docker-compose --file {{path/to/file}} up`

- Opriţi toate containerele de funcţionare:

`docker-compose stop`

- Opriți și eliminați toate containerele, rețelele, imaginile și volumele:

`docker-compose down --rmi all --volumes`

- Urmați jurnalele pentru toate containerele:

`docker-compose logs --follow`

- Urmați jurnalele pentru un anumit container:

`docker-compose logs --follow {{container_name}}`
