# pacman --remove

> Supprimes des paquets.
> Voir aussi: `pacman`.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Supprime un paquet et ses dépendances :

`sudo pacman --remove --recursive {{paquet}}`

- Supprime un paquet, ses dépendances et ses fichiers de configuration :

`sudo pacman --remove --recursive --nosave {{paquet}}`

- Supprime un paquet silencieusement :

`sudo pacman --remove --noconfirm {{paquet}}`

- Supprime les paquets orphelins (installés en tant que dépendance mais requis par aucun paquet installé) :

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Supprime un paquet et les paquets qui en dépendent :

`sudo pacman --remove --cascade {{paquet}}`

- Affiche les paquets qui seraient affectés par la commande sans agir :

`pacman --remove --print {{paquet}}`

- Affiche l'aide :

`pacman --remove --help`
