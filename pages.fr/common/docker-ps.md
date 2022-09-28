# docker ps

> Lister les conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/ps/>.

- Lister les conteneurs Docker en cours d'exécution :

`docker ps`

- Lister tous les conteneurs Docker (en cours d'exécution et arrêtés) :

`docker ps --all`

- Afficher le dernier conteneur Docker créé (avec tous les états) :

`docker ps --latest`

- Afficher les conteneurs avec une chaine de caractère dans leur nom :

`docker ps --filter="name={{name}}"`

- Afficher les conteneurs avec une même image comme parent :

`docker ps --filter "ancestor={{image}}:{{etiquette}}"`

- Afficher les conteneurs avec un code de sorti spécifique :

`docker ps --all --filter="exited={{code}}"`

- Afficher les conteneurs avec un statut spécifique (créé, en cours d'exécution, en cours de suppresion, en pause, arrêté, mort) :

`docker ps --filter="status={{status}}"`

- Afficher les conteneurs avec un point de montage spécifique :

`docker ps --filter="volume={{chemin/vers/le/dossier}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
