# docker ps

> Lister les conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Lister les conteneurs Docker en cours d'exécution :

`docker ps`

- Lister tous les conteneurs Docker (en cours d'exécution et arrêtés) :

`docker ps {{[-a|--all]}}`

- Afficher le dernier conteneur Docker créé (avec tous les états) :

`docker ps {{[-l|--latest]}}`

- Afficher les conteneurs avec une chaine de caractère dans leur nom :

`docker ps {{[-f|--filter]}} "name={{name}}"`

- Afficher les conteneurs avec une même image comme parent :

`docker ps {{[-f|--filter]}} "ancestor={{image}}:{{etiquette}}"`

- Afficher les conteneurs avec un code de sorti spécifique :

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Afficher les conteneurs avec un statut spécifique (créé, en cours d'exécution, en cours de suppresion, en pause, arrêté, mort) :

`docker ps {{[-f|--filter]}} "status={{status}}"`

- Afficher les conteneurs avec un point de montage spécifique :

`docker ps {{[-f|--filter]}} "volume={{chemin/vers/le/dossier}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
