# cp

> Copiez des fichiers et des répertoires.

- Copiez un fichier dans un autre emplacement:

`cp {{chemin/vers/fichier_source.ext}} {{chemin/vers/fichier_cible.ext}}`

- Copiez un fichier dans un autre répertoire, en conservant le nom du fichier:

`cp {{chemin/vers/fichier_source.ext}} {{chemin/vers/répertoire_parent_cible}}`

- Copiez récursivement le contenu d'un répertoire vers un autre emplacement (si la destination existe, le répertoire est copié à l'intérieur):

`cp -R {{chemin/vers/répertoire_source}} {{chemin/vers/répertoire_cible}}`

- Copiez un répertoire récursivement, en mode verbeux (affiche les fichiers au fur et à mesure de leur copie):

`cp -vR {{chemin/vers/répertoire_source}} {{chemin/vers/répertoire_cible}}`

- Copiez les fichiers texte vers un autre emplacement, en mode interactif (invite l'utilisateur avant d'écraser):

`cp -i {{*.txt}} {{chemin/vers/répertoire_cible}}`

- Déréférencer les liens symboliques avant de copier:

`cp -L {{link}} {{chemin/vers/répertoire_cible}}`
