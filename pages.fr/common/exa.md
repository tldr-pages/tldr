# exa

> Un remplacement moderne pour `ls` (Lister le contenu du répertoire).
> Plus d'information: <https://the.exa.website>.

- Lister les fichiers un par ligne :

`exa --oneline`

- Liste tous les fichiers, y compris les fichiers cachés :

`exa --all`

- Liste au format long (autorisations, propriété, taille et date de modification) de tous les fichiers :

`exa --long --all`

- Répertorier les fichiers avec le plus gros en haut :

`exa --reverse --sort={{taille}}`

- Afficher une arborescence de fichiers, sur trois niveaux de profondeur :

`exa --long --tree --level={{3}}`

- Liste des fichiers triés par date de modification (le plus ancien en premier) :

`exa --long --sort={{modifié}}`

- Répertorier les fichiers avec leur en-tête, leur icône et leur statut Git :

`exa --long --header --icons --git`

- Ne listez pas les fichiers mentionnés dans `.gitignore` :

`exa --git-ignore`
