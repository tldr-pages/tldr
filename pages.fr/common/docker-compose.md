# docker-compose

> Exécute et gère des applications au travers de plusieurs conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/compose/reference/>.

- Liste tous les conteneurs en cours d'exécution :

`docker-compose ps`

- Crée et démarre en arrière-plan tous les conteneurs décrits dans le fichier `docker-compose.yml` du répertoire courant :

`docker-compose up -d`

- Démarre tous les conteneurs après les avoir recréés si nécessaire :

`docker-compose up --build`

- Démarre tous les conteneurs spécifiés dans un fichier compose alternatif :

`docker-compose --file {{chemin/vers/fichier}} up`

- Arrête tous les conteneurs en cours d'exécution :

`docker-compose stop`

- Arrête et supprime tous les conteneurs, réseaux, images et volumes :

`docker-compose down --rmi all --volumes`

- Affiche et suit la journalisation de tous les conteneurs :

`docker-compose logs --follow`

- Affiche et suit la journalisation pour un conteneurs spécifique :

`docker-compose logs --follow {{nom_container}}`
