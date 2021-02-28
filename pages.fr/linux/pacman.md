# pacman

> Outil de gestion de paquets sur Arch Linux.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`pacman -Syu`

- Installe un nouveau paquet :

`pacman -S {{nom_paquet}}`

- Efface un paquet et ses dépendances :

`pacman -Rs {{nom_paquet}}`

- Recherche dans la base de données des paquets une expression régulière ou mot clé :

`pacman -Ss "{{terme_recherche}}"`

- Liste les paquets installés et leurs versions :

`pacman -Q`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman -Qe`

- Trouve à quel paquet un certain fichier appartient :

`pacman -Qo {{fichier}}`

- Vide le cache des paquets pour libérer de l'espace :

`pacman -Scc`
