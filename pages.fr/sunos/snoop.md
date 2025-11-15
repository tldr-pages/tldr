# snoop

> Renifleur de paquets réseau.
> Équivalent SunOS de tcpdump.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capturer des paquets sur une interface réseau spécifique :

`snoop -d {{e1000g0}}`

- Enregistrer les paquets capturés dans un fichier au lieu de les afficher :

`snoop -o {{nom_de_fichier}}`

- Afficher le résumé détaillé de la couche de protocole des paquets d'un fichier :

`snoop -V -i {{nom_de_fichier}}`

- Capturez les paquets réseau provenant d'un nom d'hôte et accédez à un port donné :

`snoop to port {{port}} from host {{nom_d'hôte}}`

- Capturez et affichez un vidage hexadécimal des paquets réseau échangés entre deux adresses IP :

`snoop -x0 -p4 {{adresse_ip_1}} {{adresse_ip_2}}`
