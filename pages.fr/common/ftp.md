# ftp

> Outils permettant d'interragir avec un serveur avec le protocole FTP.

- Se connecter à un serveur FTP :

`ftp {{ftp.exemple.com}}`

- Passer au mode de transfert binaire (medias, fichiers compressés, etc) :

`binary`

- Transférer plusieurs fichiers sans demander de confirmation pour chaque :

`prompt off`

- Télécharger plusieurs fichiers :

`mget {{*.png}}`

- Uploader plusieurs fichiers :

`mput {{*.zip}}`

- Supprimer plusieurs fichiers sur le serveur distant :

`mdelete {{*.txt}}`

- Renommer un fichier sur le serveur distant :

`rename {{ancien_fichier}} {{nouveau_fichier}}`
