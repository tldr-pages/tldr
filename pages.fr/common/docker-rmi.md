# docker rmi

> Supprimer une ou plusieurs images Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Afficher l'aide :

`docker rmi`

- Supprimer une ou plusieurs images en fonction de leurs noms :

`docker rmi {{image1 image2 ...}}`

- Supprimer une image en forçant la suppression :

`docker rmi --force {{image}}`

- Supprimer une image sans supprimer les parents non étiquetés :

`docker rmi --no-prune {{image}}`
