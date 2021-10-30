# docker container

> Gère les conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/container/>.

- Liste les conteneurs Dockers en cours d'exécution :

`docker container ls`

- Démarre un ou plusieurs conteneur arrêtés :

`docker container start {{nom_conteneur_1}} {{nom_conteneur_2}}`

- Tue un ou plusieurs conteneurs en cours d'exécution :

`docker container kill {{nom_conteneur}}`

- Arrête un ou plusieurs conteneurs en cours d'exécution :

`docker container stop {{nom_conteneur}}`

- Mets en pause tous les processus d'un ou plusieurs conteneurs :

`docker container pause {{nom_conteneur}}`

- Affiche des informations détaillées sur un ou plusieurs conteneurs :

`docker container inspect {{nom_conteneur}}`

- Exporte le système de fichiers d'un conteneur sous forme d'archive Tar :

`docker container export {{nom_conteneur}}`

- Crée une nouvelle image à partir des changements d'un conteneur :

`docker container commit {{nom_conteneur}}`
