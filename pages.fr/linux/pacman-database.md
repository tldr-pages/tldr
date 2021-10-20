# pacman --database

> Interagis avec les bases de données des paquets Arch Linux.
> Modifie des attributs des paquets installés.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Affiche l'aide :

`pacman --database --help`

- Marque un paquet comme étant installé en tant que dépendance :

`sudo pacman --database --asdeps {{paquet}}`

- Marque un paquet comme étant explicitement installé :

`sudo pacman --database --asexplicit {{paquet}}`

- Vérifie les dépendances de tous les paquets installés :

`pacman --database --check`

- Vérifie que toutes les dépendances des paquets installés sont disponibles dans les dépôts :

`pacman --database --check --check`

- N'affiche que les messages d'erreur :

`pacman --database --check --quiet`
