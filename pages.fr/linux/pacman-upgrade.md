# pacman --upgrade

> Outil de gestion de paquets d'Arch Linux.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Afficher l'aide :

`pacman --upgrade --help`

- Installer un ou des paquets depuis le système de fichiers :

`sudo pacman --upgrade {{chemin/vers/paquet1.pkg.tar.zst}} {{chemin/vers/paquet2.pkg.tar.zst}}`

- Installer un paquet silencieusement :

`sudo pacman --upgrade --noconfirm {{chemin/vers/paquet.pkg.tar.zst}}`

- Ecrire par dessus les fichiers en conflit pendant l'installation du paquet :

`sudo pacman --upgrade --overwrite {{chemin/vers/fichier}} {{chemin/vers/paquet.pkg.tar.zst}}`

- Installer un paquet sans vérifier les dépendances :

`sudo pacman --upgrade --nodeps {{chemin/vers/paquet.pkg.tar.zst}}`

- Afficher ce qui se passerait si la commande était exécutée mais sans agir :

`pacman --query --print {{chemin/vers/paquet.pkg.tar.zst}}`
