# docker container ls

> Liste les conteneurs Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Liste les conteneurs Docker en cours d'exécution :

`docker {{[ps|container ls]}}`

- Liste tous les conteneurs Docker (en cours d'exécution et arrêtés) :

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Affiche le dernier conteneur Docker créé (avec tous les états) :

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Affiche les conteneurs avec une chaine de caractère dans leur nom :

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{nom}}"`

- Affiche les conteneurs avec une même image comme parent :

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{etiquette}}"`

- Affiche les conteneurs avec un code de sorti spécifique :

`docker {{[ps|container ls]}} {{[-f|--filter]}} "exited={{code}}" {{[-a|--all]}}`

- Affiche les conteneurs avec un statut spécifique (créé, en cours d'exécution, en cours de suppresion, en pause, arrêté, mort) :

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{statut}}"`

- Affiche les conteneurs avec un point de montage spécifique :

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{chemin/vers/répertoire}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
