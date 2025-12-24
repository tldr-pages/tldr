# docker container run

> Exécuter une commande dans un nouveau conteneur Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/run/>.

- Exécute une commande dans un nouveau conteneur Docker avec une image étiquetée :

`docker run {{image:etiquette}} {{commande}}`

- Exécute une commande dans un nouveau conteneur Docker en mode détaché (en arrière-plan) et affiche l'ID du conteneur :

`docker run {{[-d|--detach]}} {{image}} {{commande}}`

- Exécute une command dans un conteneur éphémère avec une mode interactif et un terminal pseudo-TTY :

`docker run --rm {{[-it|--interactive --tty]}} {{image}} {{commande}}`

- Exécute une commande dans un nouveau conteneur avec des variables d'environnement :

`docker run {{[-e|--env]}} '{{variable}}={{valuer}}' {{[-e|--env]}} {{variable}} {{image}} {{commande}}`

- Exécute une commande dans un nouveau conteneur avec des volumes montés :

`docker run {{[-v|--volume]}} {{/chemin/vers/l_hote}}:{{chemin/vers/le/conteneur}} {{image}} {{commande}}`

- Exécute une commande dans un nouveau conteneur avec des ports publiés :

`docker run {{[-p|--publish]}} {{port_de_l_hote}}:{{port_du_conteneur}} {{image}} {{commande}}`

- Exécute une commande dans un nouveau conteneur en écrasant l'entrée du point d'entrée de l'image :

`docker run --entrypoint {{commande}} {{image}}`

- Exécute une commande dans un nouveau conteneur en le connectant à un réseau :

`docker run --network {{reseau}} {{image}}`
