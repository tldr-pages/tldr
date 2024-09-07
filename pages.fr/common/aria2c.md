# aria2c

> Utilitaire de téléchargement.
> Supporte HTTP(S), FTP, SFTP, BitTorrent, et Metalink.
> Plus d'informations : <https://aria2.github.io>.

- Télécharge depuis une URI vers un fichier :

`aria2c "{{url}}"`

- Télécharge un fichier via l'url spécifié en choisissant le nom de ce dernier :

`aria2c --out {{nom_de_fichier}} "{{url}}"`

- Télécharge plusieurs fichiers (différents) en parallèle :

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- Télécharge depuis plusieurs sources avec chaque URI pointant vers le même fichier :

`aria2c "{{url1 url2 ...}}"`

- Télécharge les URIs listées dans un fichier avec un nombre limité de téléchargements en parallèle :

`aria2c --input-file={{nom_de_fichier}} --max-concurrent-downloads={{nombre_de_téléchargements}}`

- Télécharge avec plusieurs connections :

`aria2c --split {{nombre_de_connections}} "{{url}}"`

- Téléchargement FTP avec nom d'utilisateur et mot de passe :

`aria2c --ftp-user={{nom_d_utilisateur}} --ftp-passwd={{mot_de_passe}} "{{url}}"`

- Limite la vitesse de téléchargement en octets/s :

`aria2c --max-download-limit={{vitesse}} "{{url}}"`
