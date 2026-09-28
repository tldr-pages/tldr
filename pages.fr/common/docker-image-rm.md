# docker image rm

> Supprime une ou plusieurs images Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Supprime une ou plusieurs images en fonction de leurs noms :

`docker {{[rmi|image rm]}} {{image1 image2 ...}}`

- Supprime une image en forçant la suppression :

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{image}}`

- Supprime une image sans supprimer les parents non étiquetés :

`docker {{[rmi|image rm]}} --no-prune {{image}}`

- Affiche l'aide :

`docker {{[rmi|image rm]}} --help`
