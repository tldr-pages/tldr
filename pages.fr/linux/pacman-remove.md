# pacman --remove

> Outil de gestion de paquets d'Arch Linux.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Afficher l'aide :

`pacman --remove --help`

- Supprimer un paquet et ses dépendances :

`sudo pacman --remove --recursive {{paquet}}`

- Supprimer un paquet, ses dépendances et ses fichiers de configuration :

`sudo pacman --remove --recursive --nosave {{package_name}}`

- Supprimer un paquet silencieusement :

`sudo pacman --remove --noconfirm {{package_name}}`

- Supprimer les paquets orphelins (installés en tant que dépendance mais requis par aucun paquet installé) :

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Supprimer un paquet et les paquets qui en dépendent :

`sudo pacman --remove --cascade {{package_name}}`

- Afficher les paquets qui seraient affectés par la commande sans agir :

`pacman --remove --print {{package_name}}`
