# df

> Montre un aperçu de l'utilisation de l'espace disque.
> Plus d'informations : <https://manned.org/df.1posix>.

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque :

`df`

- Afficher tous les systèmes de fichiers et leur utilisation d'espace disque dans un format plus facilement :

`df -h`

- Afficher le système de fichiers et son utilisation d'espace disque rattaché au chemin donné :

`df {{chemin/vers/fichier_ou_dossier}}`

- Afficher des statistiques sur le nombre d'inodes disponibles :

`df -i`

- Afficher les systèmes de fichiers sauf ceux de types spécifiques :

`df -x {{squashfs}} -x {{tmpfs}}`
