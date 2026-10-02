# pacman --database

> Interagit avec les bases de données des paquets Arch Linux.
> Modifie certains attributs des paquets installés.
> Plus d'informations : <https://manned.org/pacman.8>.

- Marque un paquet comme étant installé en tant que dépendance :

`sudo pacman -D --asdeps {{paquet}}`

- Marque un paquet comme étant explicitement installé :

`sudo pacman -D --asexplicit {{paquet}}`

- Vérifie les dépendances de tous les paquets installés :

`pacman -Dk`

- Vérifie que toutes les dépendances des paquets installés sont disponibles dans les dépôts :

`pacman -Dkk`

- N'affiche que les messages d'erreur :

`pacman -Dkq`

- Affiche l'aide :

`pacman -Dh`
