# docker exec

> Exécute une commande dans un conteneur déjà en cours d'exécution.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/exec/>.

- Entrer dans un shell interactif dans un conteneur en cours d'exécution :

`docker exec --interactive --tty {{nom_du_conteneur}} {{/bin/bash}}`

- Exécuter une commande en arrière-plan (détachée) dans un conteneur en cours d'exécution :

`docker exec --detach {{nom_du_conteneur}} {{commande}}`

- Sélectionner le répertoire de travail pour une commande donnée à exécuter :

`docker exec --interactive -tty --workdir {{chemin/vers/le/répertoire}} {{nom_du_conteneur}} {{commande}}`

- Exécuter une commande en arrière-plan sur un conteneur existant mais garder `stdin` ouvert :

`docker exec --interactive --detach {{nom_du_conteneur}} {{commande}}`

- Définir une variable d'environnement dans une session Bash en cours d'exécution :

`docker exec --interactive --tty --env {{variable_d_environnement}}={{valeur}} {{nom_du_conteneur}} {{/bin/bash}}`

- Exécuter une commande en tant qu'utilisateur spécifique :

`docker exec --user {{utilisateur}} {{nom_du_conteneur}} {{commande}}`
