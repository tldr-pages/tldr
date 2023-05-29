# pacman

> Outil de gestion de paquets sur Arch Linux.
> Voir aussi: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`sudo pacman -Syu`

- Installe un nouveau paquet :

`sudo pacman -S {{nom_paquet}}`

- Efface un paquet et ses dépendances :

`sudo pacman -Rs {{nom_paquet}}`

- Recherche dans la base de données des paquets une expression régulière ou mot clé :

`pacman -Ss "{{terme_recherche}}"`

- Liste les paquets installés et leurs versions :

`pacman -Q`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman -Qe`

- Trouve à quel paquet un certain fichier appartient :

`pacman -Qo {{fichier}}`

- Vide le cache des paquets pour libérer de l'espace :

`sudo pacman -Scc`
