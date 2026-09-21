# aria2c

> Utilitaire de téléchargement rapide.
> Supporte HTTP(S), FTP, SFTP, BitTorrent, et Metalink.
> Voir aussi : `axel`.
> Plus d'informations : <https://aria2.github.io/manual/en/html/aria2c.html>.

- Télécharge depuis une URI spécifique vers un fichier :

`aria2c "{{url}}"`

- Télécharge un fichier via une URI avec un nom de sortie spécifique :

`aria2c {{[-o|--out]}} {{chemin/vers/fichier}} "{{url}}"`

- Télécharge plusieurs fichiers différents en parallèle :

`aria2c {{[-Z|--force-sequential=true]}} {{"url1" "url2" ...}}`

- Télécharge le même fichier depuis différents miroirs et vérifie la somme de contrôle du fichier téléchargé :

`aria2c --checksum {{sha-256}}={{hash}} {{"url1" "url2" ...}}`

- Télécharge les URIs listées dans un fichier avec un nombre spécifique de téléchargements en parallèle :

`aria2c {{[-i|--input-file]}} {{chemin/vers/fichier}} {{[-j|--max-concurrent-downloads]}} {{nombre_telechargements}}`

- Télécharge avec plusieurs connexions :

`aria2c {{[-s|--split]}} {{nombre_connexions}} "{{url}}"`

- Téléchargement FTP avec nom d'utilisateur et mot de passe :

`aria2c --ftp-user {{nom_d_utilisateur}} --ftp-passwd {{mot_de_passe}} "{{url}}"`

- Limite la vitesse de téléchargement en octets/s :

`aria2c --max-download-limit {{vitesse}} "{{url}}"`
