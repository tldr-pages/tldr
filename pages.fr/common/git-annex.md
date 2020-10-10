# git annex

> Gérez les fichiers avec git, sans archiver leur contenu.
> Lorsqu'un fichier est annexé, son contenu est déplacé dans un stockage clé-valeur et un lien symbolique est créé qui pointe vers le contenu.
> Plus d information: <https://git-annex.branchable.com>.

- Aide:

`git annex help`

- Initialize le repo avec git annex:

`git annex init`

- Ajoute un fichier:

`git annex add {{path/to/file_or_directory}}`

- Affiche le statut courrand d un fichier ou repertoire:

`git annex status {{path/to/file_or_directory}}`

- Synchronise un repository local avec un distant:

`git annex {{remote}}`

- Recupére un ficheir ou un repertoire:

`git annex get {{path/to/file_or_directory}}`
