# exa

> Une alternative moderne à `ls` (pour lister le contenu de répertoires).
> Plus d'informations : <https://github.com/ogham/exa#command-line-options>.

- Liste les fichiers, un par ligne :

`exa {{[-1|--oneline]}}`

- Liste tous les fichiers, y compris les fichiers cachés :

`exa {{[-a|--all]}}`

- Liste au format long (autorisations, propriété, taille et date de modification) de tous les fichiers :

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Liste les fichiers avec le plus volumineux en haut :

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Affiche une arborescence de fichiers, sur trois niveaux de profondeur :

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Liste des fichiers triés par date de modification (le plus ancien en premier) :

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Liste les fichiers avec leur en-tête, leur icône et leur statut Git :

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- Liste les fichiers sauf ceux mentionnés dans `.gitignore` :

`exa --git-ignore`
