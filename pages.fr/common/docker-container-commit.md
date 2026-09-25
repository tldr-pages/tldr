# docker container commit

> Crée une nouvelle image depuis les changements d'un conteneur.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Crée une image à partir d'un conteneur spécifique :

`docker {{[commit|container commit]}} {{conteneur}} {{image}}:{{etiquette}}`

- Applique une instruction `CMD` du Dockerfile à l'image créée :

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{commande}}" {{conteneur}} {{image}}:{{etiquette}}`

- Applique une instruction `ENV` du Dockerfile à l'image créée :

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{name}}={{value}}" {{conteneur}} {{image}}:{{etiquette}}`

- Crée une image avec un auteur spécifique dans les métadonnées :

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{auteur}}" {{conteneur}} {{image}}:{{etiquette}}`

- Crée une image avec un commentaire spécifique dans les métadonnées :

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{commentaire}}" {{conteneur}} {{image}}:{{etiquette}}`

- Crée une image sans mettre en pause le conteneur pendant la création :

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{conteneur}} {{image}}:{{etiquette}}`

- Affiche l'aide :

`docker {{[commit|container commit]}} --help`
