# pacman --sync

> Synchronise les paquets.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Installe un nouveau paquet :

`sudo pacman --sync {{paquet}}`

- Synchronise et mettre à jour :

`sudo pacman --sync --refresh --sysupgrade`

- Synchronise, mets à jour et installe un paquet sans demander de confirmation :

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{paquet}}`

- Recherche un paquet en utilisant un nom ou une expression régulière :

`pacman --sync --search "{{motif}}"`

- Affiche des informations sur un paquet :

`pacman --sync --info {{paquet}}`

- Ecris par dessus des fichiers pendant une mise à jour :

`sudo pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- Synchronise et mets à jour les paquets, en ignorant un paquet (peut être utilisé plusieurs fois) :

`sudo pacman --sync --refresh --sysupgrade --ignore {{paquet}}`

- Supprime les fichiers concernant des paquets non installés et les dépôts supprimés du cache de pacman :

`sudo pacman --sync --clean`
