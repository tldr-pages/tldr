# airmon-ng

> Active le mode surveillance sur les appareils sans fils.
> Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Liste les appareils sans fils et leurs statuts :

`sudo airmon-ng`

- Allume le mode surveillance sur un appareil spécifique :

`sudo airmon-ng start {{wlan0}}`

- Tue les processus nuisibles qui utilisent les appareils sans fils :

`sudo airmon-ng check kill`

- Éteint le mode surveillance pour une interface réseau spécifique :

`sudo airmon-ng stop {{wlan0mon}}`
