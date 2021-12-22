# docker

> Gestion des conteneurs et des images Docker.
> Certaines commandes comme `docker run` ont leur propre documentation.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/cli/>.

- Liste tous les conteneurs Docker (en cours d'exécution ou arrêtés) :

`docker ps --all`

- Démarre un conteneur à partir d'une image, avec un nom personnalisé :

`docker run --name {{nom_conteneur}} {{image}}`

- Démarre ou arrête un conteneur existant :

`docker {{start|stop}} {{nom_conteneur}}`

- Télécharge une image depuis un registre Docker :

`docker pull {{image}}`

- Affiche les images déjà téléchargées :

`docker images`

- Ouvre un shell dans un conteneur déjà en cours d'exécution :

`docker exec -it {{nom_conteneur}} {{sh}}`

- Supprime un conteneur arrêté :

`docker rm {{nom_conteneur}}`

- Récupère et suit les journaux de message d'un conteneur :

`docker logs -f {{nom_conteneur}}`
