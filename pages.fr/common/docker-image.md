# docker image

> Gérer les images Docker.
> Voir aussi : `docker build`, `docker image pull`, `docker image rm`.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/>.

- Lister les images Docker locales :

`docker {{[images|image ls]}}`

- Supprimer les images Docker locales inutilisées :

`docker image prune`

- Supprimer toutes les images inutilisées (pas seulement celles sans étiquette) :

`docker image prune {{[-a|--all]}}`

- Afficher l'historique d'une image Docker locale :

`docker {{[history|image history]}} {{image}}`
