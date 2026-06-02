# podman-compose

> Exécute et gère des conteneurs définis selon la spécification Compose.
> Plus d'informations : <https://github.com/containers/podman-compose>.

- Liste tous les conteneurs en cours d'exécution :

`podman-compose ps`

- Crée et démarre tous les conteneurs en arrière-plan en utilisant un fichier `docker-compose.yml` local :

`podman-compose up {{[-d|--detach]}}`

- Démarre tous les conteneurs en les construisant si nécessaire :

`podman-compose up --build`

- Démarre tous les conteneurs en utilisant un fichier compose alternatif :

`podman-compose {{[-f|--file]}} {{chemin/vers/fichier.yaml}} up`

- Arrête tous les conteneurs en cours d'exécution :

`podman-compose stop`

- Supprime tous les conteneurs, réseaux et volumes :

`podman-compose down {{[-v|--volumes]}}`

- Suit les journaux d'un conteneur (omettre tous les noms de conteneurs) :

`podman-compose logs {{[-f|--follow]}} {{nom_conteneur}}`

- Exécute une commande ponctuelle dans un service sans ports associés :

`podman-compose run {{nom_service}} {{commande}}`
