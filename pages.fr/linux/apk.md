# apk

> Gestionnaire de paquet d'Alpine Linux.
> Plus d'informations: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Mettre à jour les indexes de tous les dêpots distants:

`apk update`

- Installer un nouveau paquet:

`apk add {{paquet}}`

- Désinstaller un paquet:

`apk del {{paquet}}`

- Essayer de réparer un paquet ou mettre à jour un paquet sans ses dépendances:

`apk fix {{paquet}}`

- Rechercher des paquets à partir d'un mot-clé:

`apk search {{mot_cle}}`

- Obtenir des information à propos d'un paquet précis:

`apk info {{paquet}}`
