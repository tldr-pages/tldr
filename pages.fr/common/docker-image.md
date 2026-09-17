# docker image

> Gére les images Docker.
> Voir aussi : `docker build`, `docker image pull`, `docker image rm`.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/>.

- Liste les images Docker locales :

`docker {{[images|image ls]}}`

- Supprime les images Docker locales inutilisées :

`docker image prune`

- Supprime toutes les images inutilisées (pas seulement celles sans étiquette) :

`docker image prune {{[-a|--all]}}`

- Affiche l'historique d'une image Docker locale :

`docker {{[history|image history]}} {{image}}`
