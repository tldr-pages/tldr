# aireplay-ng

> Injecte des paquets dans un réseau sans fil.
> Fait partie de la suite logicielle réseau Aircrack-ng.
> Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Envoie un nombre spécifique de paquets de dissociation en fonction de l'adresse MAC d'un point d'accès, de l'adresse MAC d'un client et d'une interface :

`sudo aireplay-ng --deauth {{nombre}} --bssid {{mac_pa}} --dmac {{mac_client}} {{interface}}`
