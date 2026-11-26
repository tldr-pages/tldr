# git rm

> Supprime des fichiers de l'index du dépôt et du système de fichiers local.
> Plus d'informations : <https://git-scm.com/docs/git-rm>.

- Supprime un fichier de l'index du dépôt et du système de fichiers :

`git rm {{chemin/vers/fichier}}`

- Supprime un répertoire [r]écursivement :

`git rm -r {{chemin/vers/répertoire}}`

- Supprime un fichier de l'index du dépôt mais le conserve sur le système de fichiers :

`git rm --cached {{chemin/vers/fichier}}`

- Réduit le dépôt à seulement le répertoire `.git` :

`git rm -r .`
