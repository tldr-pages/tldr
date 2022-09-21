# docker commit

> Créer une nouvelle image depuis les changement d'un conteneur.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/commit/>.

- Créer une image à partir d'un conteneur spécifique :

`docker commit {{container}} {{image}}:{{tag}}`

- Appliquer une instruction `CMD` du Dockerfile à l'image créée :

`docker commit --change="CMD {{command}}" {{container}} {{image}}:{{tag}}`

- Appliquer une instruction `ENV` du Dockerfile à l'image créée :

`docker commit --change="ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Créer une image avec un auteur spécifique dans les métadonnées :

`docker commit --author="{{author}}" {{container}} {{image}}:{{tag}}`

- Créer une image avec un commentaire spécifique dans les métadonnées :

`docker commit --message="{{comment}}" {{container}} {{image}}:{{tag}}`

- Créer une image sans mettre en pause le conteneur pendant la création :

`docker commit --pause={{false}} {{container}} {{image}}:{{tag}}`

- Afficher l'aide :

`docker commit --help`
