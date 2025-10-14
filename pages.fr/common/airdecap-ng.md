# airdecap-ng

> Décrypte un fichier de capture WEP, WPA ou WPA2 chiffré.
> Fait partie de la suite logicielle réseau Aircrack-ng.
> Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Supprime les en-têtes sans fil d'un fichier de capture réseau ouvert et utilise l'adresse MAC du point d'accès pour filtrer :

`airdecap-ng -b {{mac_pa}} {{chemin/vers/capture.cap}}`

- Décrypte un fichier de capture [w]EP chiffré en utilisant la clé au format hexadécimal :

`airdecap-ng -w {{clé_hex}} {{chemin/vers.cap}}`

- Décrypte un fichier de capture WPA/WPA2 chiffré à l'aide de l'[e]ssid et du mot de [p]asse du point d'accès :

`airdecap-ng -e {{essid}} -p {{mot_de_passe}} {{chemin/vers.cap}}`

- Décrypte un fichier de capture WPA/WPA2 chiffré en préservant les en-têtes à l'aide de l'[e]ssid et du mot de [p]asse du point d'accès :

`airdecap-ng -l -e {{essid}} -p {{mot_de_passe}} {{chemin/vers.cap}}`

- Décrypte un fichier de capture WPA/WPA2 chiffré à l'aide de l'[e]ssid et du mot de [p]asse du point d'accès et utilise son adresse MAC pour filtrer :

`airdecap-ng -b {{mac_pa}} -e {{essid}} -p {{mot_de_passe}} {{chemin/vers/capture.cap}}`
