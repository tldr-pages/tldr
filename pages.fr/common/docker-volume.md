# docker volume

> Gérer les volumes de Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/volume/>.

- Créer un volume :

`docker volume create {{nom_du_volume}}`

- Créer un volume avec une étiquette spécifique :

`docker volume create --label {{étiuette}} {{nom_du_volume}}`

- Créer un volume `tmpfs` avec une taille de 100 Mo et un uid de 1000 :

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{nom_du_volume}}`

- Lister tous les volumes :

`docker volume ls`

- Supprimer un volume :

`docker volume rm {{nom_du_volume}}`

- Afficher des informations sur un volume :

`docker volume inspect {{nom_du_volume}}`

- Supprimer tous les volumes locaux non utilisés :

`docker volume prune`

- Afficher l'aide pour une sous-commande :

`docker volume {{sous_commande}} --help`
