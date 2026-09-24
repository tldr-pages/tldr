# docker container cp

> Copie des fichiers ou des répertoires entre les systèmes de fichiers hôte et conteneur.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/cp/>.

- Copie un fichier ou un répertoire de l'hôte vers un conteneur :

`docker {{[cp|container cp]}} {{chemin/vers/fichier_ou_répertoire_de_l_hote}} {{nom_du_conteneur}}:{{chemin/vers/fichier_ou_répertoire_du_conteneur}}`

- Copie un fichier ou un répertoire d'un conteneur vers l'hôte :

`docker {{[cp|container cp]}} {{nom_du_conteneur}}:{{chemin/vers/fichier_ou_répertoire_du_conteneur}} {{chemin/vers/fichier_ou_répertoire_de_l_hote}}`

- Copie un fichier ou un répertoire de l'hôte vers un conteneur, en suivant les liens symboliques (copie les fichiers liés directement, pas les liens symboliques eux-mêmes) :

`docker {{[cp|container cp]}} {{[-L|--follow-link]}} {{chemin/vers/lien_symbolique_de_l_hote}} {{nom_du_conteneur}}:{{chemin/vers/fichier_ou_répertoire_du_conteneur}}`
