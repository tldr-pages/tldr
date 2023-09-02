# docker cp

> Copier des fichiers ou des répertoires entre les systèmes de fichiers hôte et conteneur.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/cp>.

- Copier un fichier ou un répertoire de l'hôte vers un conteneur :

`docker cp {{chemin/vers/le_fichier_ou_le_dossier_de_l_hote}} {{nom_du_conteneur}}:{{chemin/vers/le_fichier_ou_le_dossier_de_conteneur}}`

- Copier un fichier ou un répertoire d'un conteneur vers l'hôte :

`docker cp {{nom_du_conteneur}}:{{chemin/vers/le_fichier_ou_le_dossier_de_conteneur}} {{chemin/vers/le_fichier_ou_le_dossier_de_l_hote}}`

- Copier un fichier ou un répertoire de l'hôte vers un conteneur, en suivant les liens symboliques (copie les fichiers liés directement, pas les liens symboliques eux-mêmes) :

`docker cp --follow-link {{chemin/vers/le_lien_symbolique_de_l_hote}} {{nom_du_conteneur}}:{{chemin/vers/le_fichier_ou_le_dossier_de_conteneur}}`
