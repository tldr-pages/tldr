# pacman --query

> Outil de gestion de paquets de Arch Linux.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman-key.8.fr>.

- Lister les paquets installés et leur version:

`pacman --query`

- Lister uniquement les paquets installés explicitement :

`pacman --query --explicit`

- Trouver le paquet propriétaire d'un fichier :

`pacman --query --owns {{fichier}}`

- Afficher des informations sur un paquet installé :

`pacman --query --info {{paquet}}`

- Liste les fichiers appartenant à un paquet :

`pacman --query --list {{paquet}}`

- Lister les paquets orphelins (installés en tant que dépendances mais requis par aucun paquet installé) :

`pacman --query --unrequired --deps --quiet`

- Lister les paquets installés ne se trouvant pas dans les dépôts :

`pacman --query --foreign`

- Lister les paquets périmés :

`pacman --query --upgrades`
