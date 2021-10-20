# pacman --files

> Interagis avec les bases de données de fichiers.
> Voir aussi `pkgfile`.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman.8.fr>.

- Affiche l'aide :

`pacman --files --help`

- Mets à jour les bases de données des fichiers :

`sudo pacman --files --refresh`

- Trouve les paquets contenant un fichier spécifique :

`pacman --files {{fichier}}`

- Trouve les paquets contenant un fichier spécifique en utilisant une expression régulière :

`pacman --files --regex '{{expression_reguliere}}'`

- Liste uniquement les noms de paquets :

`pacman --files --quiet {{fichier}}`

- Liste les fichiers contenus dans un paquet :

`pacman --files --list {{paquet}}`
