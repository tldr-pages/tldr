# airshare

> Transfère des données entre deux machines dans un réseau local.
> Plus d'informations : <https://airshare.readthedocs.io/en/latest/cli.html>.

- Partage des fichiers ou des répertoires :

`airshare {{code}} {{chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...}}`

- Reçoit un fichier :

`airshare {{code}}`

- Héberge un serveur de réception (pour pouvoir télécharger des fichiers via l'interface web) :

`airshare --upload {{code}}`

- Envoie des fichiers ou des répertoires a un serveur de reception :

`airshare --upload {{code}} {{chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...}}`

- Envoie les fichiers dont les chemins ont été copiés dans le presse-papiers :

`airshare --file-path {{code}}`

- Reçoit un fichier et le copie dans le presse-papier :

`airshare --clip-receive {{code}}`
