# airshare

> Transférer des données entre deux machines dans un réseau local.
> Plus d'informations : <https://airshare.rtfd.io/en/latest/cli.html>.

- Partager des fichiers ou des dossiers :

`airshare {{code}} {{chemin/vers/fichier_ou_dossier1 chemin/vers/fichier_ou_dossier2 ...}}`

- Recevoir un fichier :

`airshare {{code}}`

- Héberger un serveur de réception (utilisez ceci pour pouvoir télécharger des fichiers via l'interface web) :

`airshare --upload {{code}}`

- Envoyer des fichiers ou des dossiers a un serveur de reception :

`airshare --upload {{code}} {{chemin/vers/fichier_ou_dossier1 chemin/vers/fichier_ou_dossier2 ...}}`

- Envoyer les fichiers dont les chemins ont été copiés dans le presse-papiers :

`airshare --file-path {{code}}`

- Recevoir un fichier et le copier dans le presse-papier :

`airshare --clip-receive {{code}}`
