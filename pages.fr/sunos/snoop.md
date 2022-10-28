# snoop

> Renifleur de paquets réseau.
> Équivalent SunOS de tcpdump.
> Plus d'information : <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capturer des paquets sur une interface réseau spécifique :

`snoop -d {{e1000g0}}`

- Enregistrer les paquets capturés dans un fichier au lieu de les afficher :

`snoop -o {{filename}}`

- Afficher le résumé détaillé de la couche de protocole des paquets d'un fichier :

`snoop -V -i {{filename}}`

- Capturez les paquets réseau provenant d'un nom d'hôte et accédez à un port donné :

`snoop to port {{port}} from host {{hostname}}`

- Capturez et affichez un vidage hexadécimal des paquets réseau échangés entre deux adresses IP :

`snoop -x0 -p4 {{ip_address_1}} {{ip_address_2}}`
