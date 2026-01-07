# docker image rm

> Supprimer une ou plusieurs images Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Supprimer une ou plusieurs images en fonction de leurs noms :

`docker {{[rmi|image rm]}} {{image1 image2 ...}}`

- Supprimer une image en forçant la suppression :

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{image}}`

- Supprimer une image sans supprimer les parents non étiquetés :

`docker {{[rmi|image rm]}} --no-prune {{image}}`

- Afficher l'aide :

`docker {{[rmi|image rm]}}`
