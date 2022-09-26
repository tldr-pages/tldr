# pacman --deptest

> Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas.
> Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Affiche les noms des paquets qui ne sont pas installés dans la liste :

`pacman --deptest {{paquet1}} {{paquet2}}`

- Vérifie que le paquet installé a une version supérieure ou égale :

`pacman --deptest "{{bash>=5}}"`

- Vérifie qu'une version ultérieure du paquet est installée :

`pacman --deptest "{{bash>5}}"`

- Affiche l'aide :

`pacman --deptest --help`
