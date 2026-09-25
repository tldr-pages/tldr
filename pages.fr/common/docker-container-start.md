# docker container start

> Lance un ou plusieurs conteneurs arrêtés.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/start/>.

- Lance un conteneur Docker :

`docker {{[start|container start]}} {{conteneur}}`

- Lance un conteneur, en attachant `stdout` et `stderr` et en transférant les signaux :

`docker {{[start|container start]}} {{[-a|--attach]}} {{conteneur}}`

- Lance un ou plusieurs conteneurs séparés par des espaces :

`docker {{[start|container start]}} {{conteneur1 conteneur2 ...}}`

- Affiche l'aide :

`docker {{[start|container start]}} --help`
