# docker commit

> Créer une nouvelle image depuis les changement d'un conteneur.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Créer une image à partir d'un conteneur spécifique :

`docker commit {{conteneur}} {{image}}:{{etiquette}}`

- Appliquer une instruction `CMD` du Dockerfile à l'image créée :

`docker commit {{[-c|--change]}} "CMD {{commande}}" {{conteneur}} {{image}}:{{etiquette}}`

- Appliquer une instruction `ENV` du Dockerfile à l'image créée :

`docker commit {{[-c|--change]}} "ENV {{name}}={{value}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image avec un auteur spécifique dans les métadonnées :

`docker commit {{[-a|--author]}} "{{auteur}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image avec un commentaire spécifique dans les métadonnées :

`docker commit {{[-m|--message]}} "{{commentaire}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image sans mettre en pause le conteneur pendant la création :

`docker commit {{[-p|--pause]}} {{false}} {{conteneur}} {{image}}:{{etiquette}}`

- Afficher l'aide :

`docker commit --help`
