# pacman --deptest

> Vérifier la satisfaction des dépendances et renvoyer celles qui ne le sont pas.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Afficher les noms des paquets qui ne sont pas installés dans la liste :

`pacman --deptest {{paquet1}} {{paquet2}}`

- Vérifier que le paquet installé a une version supérieure ou égale :

`pacman --deptest "{{paquet>=version}}"`

- Vérifier qu'une version ultérieure du paquet est installée :

`pacman --deptest "{{paquet>version}}"`

- Afficher l'aide :

`pacman --deptest --help`
