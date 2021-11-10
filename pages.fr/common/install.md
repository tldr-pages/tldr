# install

> Copie des fichiers et met à jour leurs attributs.
> Copie des fichiers (souvent des exécutables) dans un répertoire système comme `/usr/local/bin` et leur donne les permissions et propriétaires appropriés.
> Plus d'informations : <https://www.gnu.org/software/coreutils/install>.

- Copie des fichiers vers une destination :

`install {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur propriétaire :

`install --owner {{utilisateur}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur groupe d'appartenance :

`install --group {{utilisateur}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur mode :

`install --mode {{+x}} {{chemin/fichier/source}} {{chemin/repertoire/destination}}`

- Copie des fichiers en mettant à jour leur dates d'accès et de modification à partir de leurs sources respectives :

`install --preserve-timestamps {{chemin/fichier/source}} {{chemin/repertoire/destination}}`
