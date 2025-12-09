# docker rm

> Supprime un ou plusieurs conteneurs.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Supprimer des conteneurs :

`docker rm {{conteneur1 conteneur2 ...}}`

- Supprimer des conteneurs par la force :

`docker rm {{[-f|--force]}} {{conteneur1 conteneur2 ...}}`

- Supprimer un conteneur et ses volumes :

`docker rm {{[-v|--volumes]}} {{conteneur}}`

- Affiche l'aide :

`docker rm {{[-h|--help]}}`
