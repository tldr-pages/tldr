# docker system

> Gérer les données Docker et afficher des informations sur l'ensemble du système.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/system/>.

- Afficher l'aide :

`docker system`

- Afficher l'utilisation du disque par docker:

`docker system df`

- Afficher des informations détaillées sur l'utilisation du disque par docker:

`docker system df --verbose`

- Supprimer les données non utilisées :

`docker system prune`

- Supprimer les données non utilisées de plus d'un temps donné dans le passé :

`docker system prune --filter="until={{heures}}h{{minutes}}m"`

- Afficher les événements du démon Docker en temps réel :

`docker system events`

- Afficher les événements du démon Docker en temps réel avec un format JSON :

`docker system events --filter 'type=container' --format '{{json .}}'`

- Afficher les informations sur le système Docker :

`docker system info`
