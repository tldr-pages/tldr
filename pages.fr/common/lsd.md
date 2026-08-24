# lsd

> Liste le contenu d'un répertoire.
> Commande `ls` de nouvelle génération, écris en Rust.
> Plus d'informations : <https://github.com/lsd-rs/lsd/blob/main/doc/lsd.md>.

- Liste les fichiers et les répertoires, un par ligne :

`lsd {{[-1|--oneline]}}`

- Liste tous les fichiers et les répertoires, ainsi que ceux cachés, du répertoire courant :

`lsd {{[-a|--all]}}`

- Liste les fichiers et les répertoires en ajoutant `/` après le nom des répertoires :

`lsd {{[-F|--classify]}}`

- Liste tous les fichiers et les répertoires dans le format long (permissions, propriétaire, taille dans un format lisible, et date de modification) :

`lsd {{[-lha|--long --human-readable --all]}}`

- Liste les fichiers et les répertoires dans le format long, triés par taille (descendent) :

`lsd {{[-lS|--long --sizesort]}}`

- Liste les fichiers et les répertoires dans le format long, triés par date de modification (plus vieux en premier) :

`lsd {{[-ltr|--long --timesort --reverse]}}`

- Liste seulement les répertoires :

`lsd {{[-d|--directory-only]}} {{*/}}`

- Liste récursivement tous les répertoires dans un format arborescent :

`lsd --tree {{[-d|--directory-only]}}`
