# docker commit

> Créer une nouvelle image depuis les changement d'un conteneur.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/commit/>.

- Créer une image à partir d'un conteneur spécifique :

`docker commit {{conteneur}} {{image}}:{{etiquette}}`

- Appliquer une instruction `CMD` du Dockerfile à l'image créée :

`docker commit --change="CMD {{commande}}" {{conteneur}} {{image}}:{{etiquette}}`

- Appliquer une instruction `ENV` du Dockerfile à l'image créée :

`docker commit --change="ENV {{name}}={{value}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image avec un auteur spécifique dans les métadonnées :

`docker commit --author="{{auteur}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image avec un commentaire spécifique dans les métadonnées :

`docker commit --message="{{commentaire}}" {{conteneur}} {{image}}:{{etiquette}}`

- Créer une image sans mettre en pause le conteneur pendant la création :

`docker commit --pause={{false}} {{conteneur}} {{image}}:{{etiquette}}`

- Afficher l'aide :

`docker commit --help`
