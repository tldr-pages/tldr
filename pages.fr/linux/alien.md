# alien

> Convertit différents paquets d'installation vers d'autres formats.
> Plus d'informations : <https://manned.org/alien>.

- Convertit un fichier d'installation spécifique vers le format Debian (extension `.deb`) :

`sudo alien --to-deb {{chemin/vers/fichier}}`

- Convertit un fichier d'installation spécifique vers le format Red Hat (extension `.rpm`) :

`sudo alien --to-rpm {{chemin/vers/fichier}}`

- Convertit un fichier d'installation spécifique en un fichier d'installation Slackware (extension `.tgz`) :

`sudo alien --to-tgz {{chemin/vers/fichier}}`

- Convertit un fichier d'installation spécifique vers le format Debian et l'installe sur le système :

`sudo alien --to-deb --install {{chemin/vers/fichier}}`
