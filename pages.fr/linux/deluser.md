# deluser

> Supprime un utilisateur du système.
> Plus d'informations : <https://manpages.debian.org/latest/adduser/deluser.html>.

- Supprime un utilisateur :

`sudo deluser {{nom_dutilisateur}}`

- Supprime un utilisateur et son répertoire "home" :

`sudo deluser --remove-home {{nom_dutilisateur}}`

- Supprime un utilisateur et son répertoire "home", mais sauvegarde ses fichiers dans une archive `.tar.gz` dans le répertoire spécifié :

`sudo deluser --backup-to {{chemin/vers/le/répertoire/de/sauvegarde}} --remove-home {{nom_dutilisateur}}`

- Supprime un utilisateur et tous les fichiers qu'il possède :

`sudo deluser --remove-all-files {{nom_dutilisateur}}`
