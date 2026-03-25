# pacman --files

> Interagis avec les bases de données de fichiers.
> Voir aussi : `pacman`, `pkgfile`.
> Plus d'informations : <https://manned.org/pacman.8>.

- Mets à jour les bases de données des fichiers :

`sudo pacman -Fy`

- Trouve les paquets contenant un fichier spécifique :

`pacman -F {{fichier}}`

- Trouve les paquets contenant un fichier spécifique en utilisant une expression régulière :

`pacman -Fx '{{expression_reguliere}}'`

- Liste uniquement les noms de paquets :

`pacman -Fq {{fichier}}`

- Liste les fichiers contenus dans un paquet :

`pacman -Fl {{paquet}}`

- Affiche l'aide :

`pacman -Fh`
