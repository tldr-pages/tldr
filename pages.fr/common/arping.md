# arping

> Découvre et sonde des hôtes dans un réseau en utilisant le protocol ARP.
> Très utile pour la découverte d'adresse MAC.
> Plus d'informations : <https://github.com/ThomasHabets/arping>.

- Ping un hôte par paquets de requête ARP :

`arping {{ip_hôte}}`

- Ping un hôte sur une interface spécifique :

`arping -I {{interface}} {{ip_hôte}}`

- Ping un hôte et arrête à la première réponse :

`arping -f {{ip_hôte}}`

- Ping un hôte un certain nombre de fois :

`arping -c {{nombre_d_appel}} {{ip_hôte}}`

- Diffuse les paquets de requête ARP pour mettre à jour les caches ARP voisin :

`arping -U {{ip_à_diffuser}}`

- Détecte les adresses IP dupliquées dans le réseau en envoyant les requêtes ARP avec une expiration de 3 secondes :

`arping -D -w {{3}} {{ip_à_vérifier}}`
