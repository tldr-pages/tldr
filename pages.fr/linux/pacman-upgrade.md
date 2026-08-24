# pacman --upgrade

> Mets à jour ou ajoute des paquets au système.
> Voir aussi : `pacman`.
> Plus d'informations : <https://manned.org/pacman.8>.

- Installe un ou des paquets depuis le système de fichiers :

`sudo pacman -U {{chemin/vers/paquet1.pkg.tar.zst chemin/vers/paquet2.pkg.tar.zst ...}}`

- Installe un paquet silencieusement :

`sudo pacman -U --noconfirm {{chemin/vers/paquet.pkg.tar.zst}}`

- Ecris par dessus les fichiers en conflit pendant l'installation du paquet :

`sudo pacman -U --overwrite {{chemin/vers/fichier}} {{chemin/vers/paquet.pkg.tar.zst}}`

- Installe un paquet sans vérifier les dépendances :

`sudo pacman -Ud {{chemin/vers/paquet.pkg.tar.zst}}`

- Affiche ce qui se passerait si la commande était exécutée mais sans agir :

`pacman -Up {{chemin/vers/paquet.pkg.tar.zst}}`

- Affiche l'aide :

`pacman -Uh`
