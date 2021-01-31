# install

> Copie des fichiers et mets à jour leurs attributs.
> Copie des fichiers (souvent des exécutables) dans un répertoire système comme `/usr/local/bin` et leur donne les permissions et propriétaires appropriés.

- Copie des fichiers vers une destination :

`install {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur propriétaire :

`install -o {{utilisateur}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur groupe d'appartenance :

`install -g {{utilisateur}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur mode :

`install -m {{+x}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers en mettant à jour leur dates d'accès et de modification à partir de leurs sources respectives :

`install -p {{chemin/fichier/source}} {{chemin/repertoire/destination}}`
