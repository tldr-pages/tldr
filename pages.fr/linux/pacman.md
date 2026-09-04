# pacman

> Outil de gestion de paquets sur Arch Linux.
> Voir aussi : `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> Pour les commandes équivalentes dans d’autres gestionnaires de paquets, consultez <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Plus d'informations : <https://manned.org/pacman.8>.

- Synchronise et mets à jour tous les paquets :

`sudo pacman -Syu`

- Installe un nouveau paquet :

`sudo pacman -S {{nom_paquet}}`

- Efface un paquet et ses dépendances :

`sudo pacman -Rs {{nom_paquet}}`

- Recherche dans la base de données des paquets contenant un certain fichier :

`pacman -F "{{nom_fichier}}"`

- Liste les paquets installés et leurs versions :

`pacman -Q`

- Liste seulement les paquets installés explicitement et leurs versions :

`pacman -Qe`

- Vide le cache des paquets pour libérer de l'espace :

`sudo pacman -Scc`
