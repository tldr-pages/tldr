# docker-machine

> Crée et gère des machines qui exécutent Docker.
> Plus d'informations : <https://github.com/docker-archive-public/docker.machine>.

- Liste les machines Docker actuellement en cours d'exécution :

`docker-machine ls`

- Crée une nouvelle machine Docker avec un nom spécifique :

`docker-machine create {{nom}}`

- Récupère les informations d'une machine Docker :

`docker-machine status {{nom}}`

- Démarre une machine Docker :

`docker-machine start {{nom}}`

- Arrête une machine Docker :

`docker-machine stop {{nom}}`

- Inspecte les informations d'une machine Docker :

`docker-machine inspect {{nom}}`
