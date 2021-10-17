# pacman --files

> Outils de gestion de paquets d'Arch Linux.
> Voir aussi `pkgfile`.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Afficher l'aide :

`pacman --files --help`

- Mettre à jour les bases de données des fichiers :

`sudo pacman --files --refresh`

- Trouver les paquets contenant un fichier spécifique :

`pacman --files {{fichier}}`

- Trouver les paquets contenant un fichier spécifique en utilisant une expression régulière :

`pacman --files --regex '{{expression_reguliere}}'`

- Lister uniquement les noms de paquets :

`pacman --files --quiet {{fichier}}`

- Lister les fichiers contenus dans un paquet :

`pacman --files --list {{paquet}}`
