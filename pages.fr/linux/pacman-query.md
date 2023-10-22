# pacman --query

> Fais des requêtes dans la base de données des paquets installés.
> Voir aussi: `pacman`.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Liste les paquets installés et leur version :

`pacman --query`

- Liste uniquement les paquets installés explicitement :

`pacman --query --explicit`

- Trouve le paquet propriétaire d'un fichier :

`pacman --query --owns {{fichier}}`

- Affiche des informations sur un paquet installé :

`pacman --query --info {{paquet}}`

- Liste les fichiers appartenant à un paquet :

`pacman --query --list {{paquet}}`

- Liste les paquets orphelins (installés en tant que dépendances mais requis par aucun paquet installé) :

`pacman --query --unrequired --deps --quiet`

- Liste les paquets installés ne se trouvant pas dans les dépôts :

`pacman --query --foreign`

- Liste les paquets périmés :

`pacman --query --upgrades`
