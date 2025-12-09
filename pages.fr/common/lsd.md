# lsd

> Liste le contenu d'un répertoire.
> Commande `ls` de nouvelle génération, écris en Rust.
> Plus d'informations : <https://github.com/Peltoche/lsd>.

- Liste les fichiers et les répertoires, un par ligne :

`lsd -1`

- Liste tous les fichiers et les répertoires, ainsi que ceux cachés, du répertoire courant :

`lsd -a`

- Liste les fichiers et les répertoires en ajoutant `/` après le nom des répertoires :

`lsd -F`

- Liste tous les fichiers et les répertoires dans le format long (permissions, propriétaire, taille dans un format lisible, et date de modification) :

`lsd -lha`

- Liste les fichiers et les répertoires dans le format long, triés par taille (descendent) :

`lsd -lS`

- Liste les fichiers et les répertoires dans le format long, triés par date de modification (plus vieux en premier) :

`lsd -ltr`

- Liste seulement les répertoires :

`lsd -d {{*/}}`

- Liste récursivement tous les répertoires dans un format arborescent :

`lsd --tree -d`
