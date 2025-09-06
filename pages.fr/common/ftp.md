# ftp

> Outils permettant d'interagir avec un serveur avec le protocole FTP.
> Plus d'informations : <https://manned.org/ftp>.

- Connexion à un serveur FTP :

`ftp {{ftp.exemple.com}}`

- Connexion à un serveur FTP en spécifiant son adresse IP et son port :

`ftp {{adresse_IP}} {{port}}`

- Passe en mode de transfert binaire (médias, fichiers compressés, etc) :

`binary`

- Transfère plusieurs fichiers sans demander de confirmation pour chaque :

`prompt off`

- Télécharge plusieurs fichiers :

`mget {{*.png}}`

- Téléverse plusieurs fichiers :

`mput {{*.zip}}`

- Supprime plusieurs fichiers sur le serveur distant :

`mdelete {{*.txt}}`

- Renomme un fichier sur le serveur distant :

`rename {{ancien_fichier}} {{nouveau_fichier}}`
