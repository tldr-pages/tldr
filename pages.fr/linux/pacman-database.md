# pacman --database

> Intéragir avec les bases de données des paquets Arch Linux.
> Modifier des attributs des paquets installés.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Afficher l'aide :

`pacman --database --help`

- Marquer un paquet comme étant installé en tant que dépendance :

`sudo pacman --database --asdeps {{paquet}}`

- Marquer un paquet comme étant explicitement installé :

`sudo pacman --database --asexplicit {{paquet}}`

- Vérifier les dépendances de tous les paquets installés :

`pacman --database --check`

- Vérifier que toutes les dépendances des paquets installés sont disponibles dans les dépôts :

`pacman --database --check --check`

- N'afficher que les messages d'erreur :

`pacman --database --check --quiet`
