# docker container rm

> Supprime un ou plusieurs conteneurs.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Supprime des conteneurs :

`docker {{[rm|container rm]}} {{conteneur1 conteneur2 ...}}`

- Supprime des conteneurs par la force :

`docker {{[rm|container rm]}} {{[-f|--force]}} {{conteneur1 conteneur2 ...}}`

- Supprime un conteneur et ses volumes :

`docker {{[rm|container rm]}} {{[-v|--volumes]}} {{conteneur}}`

- Affiche l'aide :

`docker {{[rm|container rm]}} --help`
