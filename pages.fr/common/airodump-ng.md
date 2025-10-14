# airodump-ng

> Capture les paquets et affiche des informations sur les réseaux sans fil.
> Fait partie de la suite logicielle réseau Aircrack-ng.
> Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Capture les paquets et affiche des informations sur le(s) réseau(x) sans fil sur la bande 2,4 GHz :

`sudo airodump-ng {{interface}}`

- Capture les paquets et affiche des informations sur le(s) réseau(x) sans fil sur la bande 5GHz :

`sudo airodump-ng {{interface}} --band a`

- Capture les paquets et affiche des informations sur le(s) réseau(x) sans fil sur les bandes 2,4 GHz et 5 GHz :

`sudo airodump-ng {{interface}} --band abg`

- Capture les paquets et affiche des informations sur un réseau sans fil en fonction de l'adresse MAC et du canal, et enregistre la sortie dans un fichier :

`sudo airodump-ng --channel {{canal}} --write {{chemin/vers/fichier}} --bssid {{mac}} {{interface}}`
