# pacman --sync

> Outil de gestion de paquets d'Arch Linux.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Installer un nouveau paquet :

`sudo pacman --sync {{paquet}}`

- Synchroniser et mettre à jour :

`sudo pacman --sync --refresh --sysupgrade`

- Synchroniser, mettre à jour et installer un paquet sans demander de confirmation :

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{paquet}}`

- Rechercher un paquet en utilisant un nom ou une expression régulière :

`pacman --sync --search "{{motif}}"`

- Afficher des informations sur un paquet :

`pacman --sync --info {{paquet}}`

- Ecrire par dessus des fichiers pendant une mise à jour :

`sudo pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- Synchroniser et mettre à jour les paquets, en ignorant un paquet (peut être utilisé plusieurs fois) :

`sudo pacman --sync --refresh --sysupgrade --ignore {{paquet}}`

- Supprimer les fichiers concernant des paquets non installés et les dépôts supprimés du cache de pacman :

`sudo pacman --sync --clean`
