# docker container logs

> Affiche les journaux d'un conteneur.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Affiche les journaux d'un conteneur :

`docker {{[logs|container logs]}} {{nom_conteneur}}`

- Affiche les journaux d'un conteneur en les suivant :

`docker {{[logs|container logs]}} {{nom_conteneur}} {{[-f|--follow]}}`

- Affiche les 5 dernières lignes des journaux d'un conteneur :

`docker {{[logs|container logs]}} {{nom_conteneur}} {{[-n|--tail]}} 5`

- Affiche les journaux d'un conteneur avec l'horodatage :

`docker {{[logs|container logs]}} {{nom_conteneur}} {{[-t|--timestamps]}}`

- Affiche les journaux d'un conteneur depuis un certain temps (i.e. 23m, 10s, 2013-01-02T13:23:37) :

`docker {{[logs|container logs]}} {{nom_conteneur}} --until {{temps}}`
