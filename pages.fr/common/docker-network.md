# docker network

> Crée et gére des réseaux Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/network/>.

- Liste tous les réseaux disponible et configuré du service Docker :

`docker network ls`

- Crée un réseau défini par l'utilisateur :

`docker network create {{[-d|--driver]}} {{nom_du_driver}} {{nom_du_reseau}}`

- Affiche les informations détaillées des réseaux séparés par des espaces :

`docker network inspect {{nom_du_reseau}}`

- Connecte un conteneur à un réseau en utilisant un nom ou un ID :

`docker network connect {{nom_du_reseau}} {{nom_du_conteneur|id}}`

- Déconnecte un conteneur d'un réseau en utilisant un nom ou un ID :

`docker network disconnect {{nom_du_reseau}} {{nom_du_conteneur|id}}`

- Supprime tous les réseaux non utilisés (non reliés à un conteneur) :

`docker network prune`

- Supprime les réseaux séparés par des espaces :

`docker network rm {{nom_du_reseau}}`
