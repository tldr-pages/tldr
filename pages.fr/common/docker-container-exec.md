# docker container exec

> Exécute une commande dans un conteneur déjà en cours d'exécution.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Entre dans un shell interactif dans un conteneur en cours d'exécution :

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{nom_du_conteneur}} {{/bin/bash}}`

- Exécute une commande en arrière-plan (détachée) dans un conteneur en cours d'exécution :

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{nom_du_conteneur}} {{commande}}`

- Sélectionne le répertoire de travail pour une commande donnée à exécuter :

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{chemin/vers/le/répertoire}} {{nom_du_conteneur}} {{commande}}`

- Exécute une commande en arrière-plan sur un conteneur existant mais garde `stdin` ouvert :

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{nom_du_conteneur}} {{commande}}`

- Définit une variable d'environnement dans une session Bash en cours d'exécution :

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variable_d_environnement}}={{valeur}} {{nom_du_conteneur}} {{/bin/bash}}`

- Exécute une commande en tant qu'utilisateur spécifique :

`docker {{[exec|container exec]}} {{[-u|--user]}} {{utilisateur}} {{nom_du_conteneur}} {{commande}}`
