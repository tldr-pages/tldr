# docker compose

> Exécute et gère des applications au travers de plusieurs conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/compose/>.

- Liste tous les conteneurs en cours d'exécution :

`docker compose ps`

- Crée et démarre en arrière-plan tous les conteneurs décrits dans le fichier `docker-compose.yml` du répertoire courant :

`docker compose up {{[-d|--detach]}}`

- Démarre tous les conteneurs après les avoir recréés si nécessaire :

`docker compose up --build`

- Démarre tous les conteneurs en spécifiant un nom de projet et un fichier compose alternatif :

`docker compose {{[-p|--project-name]}} {{nom_de_projet}} {{[-f|--file]}} {{chemin/vers/fichier}} up`

- Arrête tous les conteneurs en cours d'exécution :

`docker compose stop`

- Arrête et supprime tous les conteneurs, réseaux, images et volumes :

`docker compose down --rmi all {{[-v|--volumes]}}`

- Affiche et suit la journalisation de tous les conteneurs :

`docker compose logs {{[-f|--follow]}}`

- Affiche et suit la journalisation pour un conteneurs spécifique :

`docker compose logs {{[-f|--follow]}} {{nom_container}}`
