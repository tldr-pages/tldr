# docker container start

> Lancer un ou plusieurs conteneurs arrêtés.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/start/>.

- Lancer un conteneur Docker :

`docker {{[start|container start]}} {{conteneur}}`

- Lancer un conteneur, en attachant `stdout` et `stderr` et en transférant les signaux :

`docker {{[start|container start]}} {{[-a|--attach]}} {{conteneur}}`

- Lancer un ou plusieurs conteneurs séparés par des espaces :

`docker {{[start|container start]}} {{conteneur1 conteneur2 ...}}`

- Afficher l'aide :

`docker {{[start|container start]}} --help`
