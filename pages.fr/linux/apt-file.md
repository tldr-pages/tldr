# apt-file

> Recherche de fichiers dans les paquets apt, y compris ceux qui ne sont pas encore installés.
> Plus d'informations : <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Mise à jour la base de données des métadonnées :

`sudo apt update`

- Recherche des paquets qui contiennent le fichier ou le chemin d'accès spécifié :

`apt-file {{search|find}} {{fichier|chemin/vers/fichier}}`

- Énumère le contenu d'un paquet spécifique :

`apt-file {{show|list}} {{nom_paquet}}`

- Cherche des paquets correspondant au motif indiqué dans l'expression régulière :

`apt-file {{search|find}} --regexp {{motif}}`
