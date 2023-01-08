# docker run

> Exécuter une commande dans un nouveau conteneur Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/run/>.

- Exécuter une commande dans un nouveau conteneur Docker avec une iamge étiquetée :

`docker run {{image:etiquette}} {{commande}}`

- Exécuter une commande dans un nouveau contenu Docker en mode détaché (en arrière-plan) et afficher l'ID du conteneur :

`docker run --detach {{image}} {{commande}}`

- Exécuter une command dans un conteneur effemère avec une mode interactif et un terminal pseudo-TTY :

`docker run --rm --interactive --tty {{image}} {{commande}}`

- Exécuter une commande dans un nouveau conteneur avec des variables d'environnement :

`docker run --env '{{variable}}={{valuer}}' --env {{variable}} {{image}} {{commande}}`

- Exécuter une commande dans un nouveau conteneur avec des volumes montés :

`docker run --volume {{/chemin/vers/l_hote}}:{{chemin/vers/le/conteneur}} {{image}} {{commande}}`

- Exécuter une commande dans un nouveau conteneur avec des ports publiés :

`docker run --publish {{port_de_l_hote}}:{{port_du_conteneur}} {{image}} {{commande}}`

- Exécuter une commande dans un nouveau conteneur en écrasant l'entrée du point d'entrée de l'image :

`docker run --entrypoint {{commande}} {{image}}`

- Exécuter une commande dans un nouveau conteneur en le connectant à un réseau :

`docker run --network {{reseau}} {{image}}`
