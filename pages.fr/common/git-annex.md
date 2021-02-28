# git annex

> Gérez les fichiers avec Git, sans archiver leur contenu.
> Lorsqu'un fichier est annexé, son contenu est déplacé dans un stockage clé-valeur et un lien symbolique est créé qui pointe vers le contenu.
> Plus d'informations : <https://git-annex.branchable.com>.

- Aide :

`git annex help`

- Initialize le repo avec Git annex :

`git annex init`

- Ajoute un fichier :

`git annex add {{chemin/vers/fichier_ou_repertoire}}`

- Affiche le statut courrand d un fichier ou repertoire :

`git annex status {{chemin/vers/fichier_ou_repertoire}}`

- Synchronise un repository local avec un distant :

`git annex {{distant}}`

- Recupére un ficheir ou un repertoire :

`git annex get {{chemin/vers/fichier_ou_repertoire}}`
