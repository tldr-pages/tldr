# docker-machine

> Créer et gérer des machines qui exécutent Docker.
> Plus d'informations: <https://docs.docker.com/machine/reference/>.

- Lister les machines Docker actuellement en cours d'exécution:

`docker-machine ls`

- Créer une nouvelle machine Docker avec un nom spécifique:

`docker-machine create {{nom}}`

- Récupérer les informations d'une machine Docker:

`docker-machine status {{nom}}`

- Démarrer une machine Docker:

`docker-machine start {{nom}}`

- Arrêter une machine Docker:

`docker-machine stop {{nom}}`

- Inspecter les informations d'une machine Docker:

`docker-machine inspect {{nom}}`
