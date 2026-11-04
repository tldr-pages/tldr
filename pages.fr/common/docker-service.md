# docker service

> Gére les services sur un démon Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/service/>.

- Liste les services sur un démon Docker :

`docker service ls`

- Crée un nouveau service :

`docker service create --name {{nom_du_service}} {{image}}:{{etiquette}}`

- Affiche des informations détaillées d'une liste de services séparée par des espaces :

`docker service inspect {{nom_du_service|id}}`

- Liste les tâches d'une liste de services séparée par des espaces :

`docker service ps {{nom_du_service|id}}`

- Redimensionne à un nombre spécifique de réplicas pour une liste de services séparée par des espaces :

`docker service scale {{nom_du_service}}={{count_of_replicas}}`

- Supprime une liste de services séparée par des espaces :

`docker service rm {{nom_du_service|id}}`
