# pacman

> Outil de gestion de paquets sur Arch Linux.
> Certaines commandes comme `pacman sync` ont leur propre documentation.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`sudo pacman --sync --refresh --sysupgrade`

- Installe un nouveau paquet :

`sudo pacman --sync {{nom_paquet}}`

- Efface un paquet et ses dépendances :

`sudo pacman --remove --recursive {{nom_paquet}}`

- Recherche dans la base de données des paquets une expression régulière ou mot clé :

`pacman --sync --search "{{terme_recherche}}"`

- Liste les paquets installés et leurs versions :

`pacman --query`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman --query --explicit`

- Trouve à quel paquet un certain fichier appartient :

`pacman --query --owns {{fichier}}`

- Vide le cache des paquets pour libérer de l'espace :

`sudo pacman --sync --clean --clean`
