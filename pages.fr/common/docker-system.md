# docker system

> Gère les données Docker et affiche des informations sur l'ensemble du système.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/system/>.

- Affiche l'utilisation du disque par Docker :

`docker system df`

- Affiche des informations détaillées sur l'utilisation du disque par Docker :

`docker system df {{[-v|--verbose]}}`

- Supprime les données non utilisées (ajouter `--volumes` pour supprimer également des volumes non utilisés):

`docker system prune`

- Supprime les données non utilisées de plus d'un temps donné dans le passé :

`docker system prune --filter "until={{heures}}h{{minutes}}m"`

- Supprime tous les données non utilisées :

`docker system prune {{[-a|--all]}} --volumes`

- Affiche les événements en temps réel du démon Docker :

`docker system events`

- Affiche les événements en temps réel des conteneurs sous forme de JSON :

`docker system events {{[-f|--filter]}} 'type=container' --format '{{json .}}'`

- Affiche les informations générales du système :

`docker system info`
