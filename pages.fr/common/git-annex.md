# git annex

> Gérez les fichiers avec Git, sans archiver leur contenu.
> Lorsqu'un fichier est annexé, son contenu est déplacé dans un stockage clé-valeur et un lien symbolique est créé qui pointe vers le contenu.
> Plus d'informations : <https://git-annex.branchable.com>.

- Initialise le dépôt :

`git annex init`

- Ajoute un fichier :

`git annex add {{chemin/vers/fichier_ou_repertoire}}`

- Affiche le statut courant d'un fichier ou répertoire :

`git annex status {{chemin/vers/fichier_ou_repertoire}}`

- Synchronise un dépôt local avec un distant :

`git annex {{distant}}`

- Récupère un fichier ou un répertoire :

`git annex get {{chemin/vers/fichier_ou_repertoire}}`

- Affiche l'aide :

`git annex help`
