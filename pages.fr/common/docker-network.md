# docker network

> Créer et gérer des réseaux Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/network/>.

- Lister tous les réseaux disponible et configuré du service Docker :

`docker network ls`

- Créer un réseau défini par l'utilisateur :

`docker network create --driver {{nom_du_driver}} {{nom_du_reseau}}`

- Afficher les informations détaillées des réseaux séparés par des espaces :

`docker network inspect {{nom_du_reseau}}`

- Connecter un conteneur à un réseau en utilisant un nom  ou  un ID :

`docker network connect {{nom_du_reseau}} {{nom_du_conteneur|ID}}`

- Déconnecter un conteneur d'un réseau en utilisant un nom ou un ID :

`docker network disconnect {{nom_du_reseau}} {{nom_du_conteneur|ID}}`

- Supprimer tous les réseaux non utilisés (non reliés à un conteneur) :

`docker network prune`

- Supprimer les réseaux séparés par des espaces :

`docker network rm {{nom_du_reseau}}`
