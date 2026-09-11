# fdupes

> Trouve les fichiers dupliqués dans les répertoires donnés.
> Plus d'informations : <https://github.com/adrianlopezroche/fdupes#introduction>.

- Cherche dans un répertoire :

`fdupes {{chemin/vers/répertoire}}`

- Cherche dans plusieurs répertoires :

`fdupes {{chemin/vers/répertoire1 chemin/vers/répertoire2 ...}}`

- Cherche dans un répertoire récursivement :

`fdupes {{[-r|--recurse]}} {{chemin/vers/répertoire}}`

- Cherche dans plusieurs répertoires dont un récursivement :

`fdupes {{chemin/vers/répertoire1}} {{[-R|--recurse:]}} {{chemin/vers/répertoire2}}`

- Cherche récursivement, en considérant les liens physiques comme des doublons :

`fdupes {{[-rH|--recurse --hardlinks]}} {{chemin/vers/répertoire}}`

- Cherche récursivement les dupliqués et demande les fichiers à conserver, supprimant les autres :

`fdupes {{[-rd|--recurse --delete]}} {{chemin/vers/répertoire}}`

- Cherche récursivement et supprime les dupliqués automatiquement :

`fdupes {{[-rdN|--recurse --delete --noprompt]}} {{chemin/vers/répertoire}}`
