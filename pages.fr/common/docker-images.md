# docker images

> Gérer les images Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/images/>.

- Lister toutes les images Docker :

`docker images`

- Lister toutes les images Docker, y compris les intermédiaires :

`docker images --all`

- Lister les images Docker en mode silencieux (seulement les IDs numériques) :

`docker images --quiet`

- Lister toutes les images Docker non utilisées par un conteneur :

`docker images --filter dangling=true`

- Lister les images Docker qui contiennent une sous-chaîne dans leur nom :

`docker images "{{*nom*}}"`
