# exa

> Une alternative moderne à `ls` (pour lister le contenu de répertoires).
> Plus d'informations : <https://the.exa.website>.

- Liste les fichiers, un par ligne :

`exa --oneline`

- Liste tous les fichiers, y compris les fichiers cachés :

`exa --all`

- Liste au format long (autorisations, propriété, taille et date de modification) de tous les fichiers :

`exa --long --all`

- Liste les fichiers avec le plus volumineux en haut :

`exa --reverse --sort={{taille}}`

- Affiche une arborescence de fichiers, sur trois niveaux de profondeur :

`exa --long --tree --level={{3}}`

- Liste des fichiers triés par date de modification (le plus ancien en premier) :

`exa --long --sort={{modifié}}`

- Liste les fichiers avec leur en-tête, leur icône et leur statut Git :

`exa --long --header --icons --git`

- Liste les fichiers sauf ceux mentionnés dans `.gitignore` :

`exa --git-ignore`
