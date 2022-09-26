# apk

> Gestionnaire de paquet d'Alpine Linux.
> Plus d'informations : <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Mets à jour les indexes de tous les dépôts distants :

`apk update`

- Installe un nouveau paquet :

`apk add {{paquet}}`

- Désinstalle un paquet :

`apk del {{paquet}}`

- Essaye de réparer un paquet ou de mettre à jour un paquet sans ses dépendances :

`apk fix {{paquet}}`

- Recherche des paquets à partir d'un mot-clé :

`apk search {{mot_cle}}`

- Obtiens des information à propos d'un paquet précis :

`apk info {{paquet}}`
