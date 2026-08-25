# arping

> Découvre et sonde des hôtes dans un réseau en utilisant le protocol ARP.
> Très utile pour la découverte d'adresse MAC.
> Plus d'informations : <https://manned.org/arping>.

- Ping un hôte par paquets de requête ARP :

`sudo arping {{ip_hôte}}`

- Ping un hôte sur une interface spécifique :

`sudo arping -I {{interface}} {{ip_hôte}}`

- Ping un hôte et arrête à la première réponse :

`sudo arping -f {{ip_hôte}}`

- Ping un hôte un certain nombre de fois :

`sudo arping -c {{nombre_d_appel}} {{ip_hôte}}`

- Diffuse les paquets de requête ARP pour mettre à jour les caches ARP voisin :

`sudo arping -U {{ip_à_diffuser}}`

- Détecte les adresses IP dupliquées dans le réseau en envoyant les requêtes ARP avec une expiration de 3 secondes :

`sudo arping -D -w {{3}} {{ip_à_vérifier}}`
