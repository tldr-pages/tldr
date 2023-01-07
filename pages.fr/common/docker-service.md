# docker service

> Gérer les services sur un démon Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/service/>.

- Lister les services sur un démon Docker :

`docker service ls`

- Créer un nouveau service :

`docker service create --name {{nom_du_service}} {{image}}:{{etiquette}}`

- Afficher des informations détaillées d'une liste de services séparée par des espaces :

`docker service inspect {{nom_du_service|ID}}`

- Lister les tâches d'une liste de services séparée par des espaces :

`docker service ps {{nom_du_service|ID}}`

- Redimensionner à un nombre spécifique de réplicas pour une liste de services séparée par des espaces :

`docker service scale {{nom_du_service}}={{count_of_replicas}}`

- Supprimer une liste de services séparée par des espaces :

`docker service rm {{nom_du_service|ID}}`
