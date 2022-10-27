# arp-scan

> Envoie des paquets ARP à des hôtes (spécifié via des adresses IP ou des noms de domaines) pour scanner le réseau local.
> Plus d'informations : <https://github.com/royhills/arp-scan>.

- Scanne le réseau local actuel :

`arp-scan --localnet`

- Scanne un réseau IP pour un masque de bits donné :

`arp-scan {{192.168.1.1}}/{{24}}`

- Scanne un réseau IP dans une plage IP :

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scanne un réseau IP pour un masque de sous-réseaux donné :

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
