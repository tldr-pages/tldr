# docker image

> Gérer les images Docker.
> Voir aussi `docker build`, `docker import`, and `docker pull`.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/image/>.

- Lister les images Docker locales :

`docker image ls`

- Supprimer les images Docker locales inutilisées :

`docker image prune`

- Supprimer toutes les images inutilisées (pas seulement celles sans étiquette) :

`docker image prune --all`

- Afficher l'historique d'une image Docker locale :

`docker image history {{image}}`
