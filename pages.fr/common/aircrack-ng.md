# aircrack-ng

> Déchiffre les clés WEP et WPA/WPA2 de l'établissement d'une liaison des paquets capturés.
> Fait partie de la suite logicielle réseau Aircrack-ng.
> Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Craque la clé du fichier de capture à l'aide d'une liste de mots :

`aircrack-ng -w {{chemin/vers/liste.txt}} {{chemin/vers/capture.cap}}`

- Craque la clé en utilisant plusieurs fils d'exécution de processeur à partir d'un fichier de capture utilisant une liste de mots :

`aircrack-ng -p {{nombre}} -w {{chemin/vers/liste.txt}} {{chemin/vers/capture.cap}}`

- Craque la clé du fichier de capture en utilisant la liste de mots et le [e]ssid du point d'accès :

`aircrack-ng -w {{chemin/vers/liste.txt}} -e {{essid}} {{chemin/vers/capture.cap}}`

- Craque la clé du fichier de capture à l'aide de la liste de mots et de l'adresse MAC du point d'accès :

`aircrack-ng -w {{chemin/vers/liste.txt}} --bssid {{mac}} {{chemin/vers/capture.cap}}`
