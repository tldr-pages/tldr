# apt-file

> Recherche de fichiers dans les paquets APT, y compris ceux qui ne sont pas encore installés.
> Plus d'informations : <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Mise à jour la base de données des métadonnées :

`sudo apt update`

- Recherche des paquets qui contiennent le fichier ou le chemin d'accès spécifié :

`apt-file search {{part/of/filename}}`

- Énumère le contenu d'un paquet spécifique :

`apt-file list {{package_name}}`
