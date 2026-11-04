# docker volume

> Gére les volumes de Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/volume/>.

- Crée un volume :

`docker volume create {{nom_du_volume}}`

- Crée un volume avec une étiquette spécifique :

`docker volume create --label {{étiquette}} {{nom_du_volume}}`

- Crée un volume `tmpfs` avec une taille de 100 Mo et un uid de 1000 :

`docker volume create {{[-o|--opt]}} {{type}}={{tmpfs}} {{[-o|--opt]}} {{device}}={{tmpfs}} {{[-o|--opt]}} {{o}}={{size=100m,uid=1000}} {{nom_du_volume}}`

- Liste tous les volumes :

`docker volume ls`

- Supprime un volume :

`docker volume rm {{nom_du_volume}}`

- Affiche des informations sur un volume :

`docker volume inspect {{nom_du_volume}}`

- Supprime tous les volumes locaux non utilisés :

`docker volume prune`

- Affiche l'aide pour une sous-commande :

`docker volume {{sous_commande}} --help`
