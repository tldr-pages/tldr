# docker image ls

> Gérer les images Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Lister toutes les images Docker :

`docker {{[images|image ls]}}`

- Lister toutes les images Docker, y compris les intermédiaires :

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Lister les images Docker en mode silencieux (seulement les IDs numériques) :

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Lister toutes les images Docker non utilisées par un conteneur :

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Lister les images Docker qui contiennent une sous-chaîne dans leur nom :

`docker {{[images|image ls]}} "{{*nom*}}"`
