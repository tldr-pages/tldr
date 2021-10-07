# ip

> Affiche / manipule l'adressage, le routage, les interfaces et périphériques réseau, les règles de routage et les tunnels.
> Certaines commandes comme `ip address` ont leur propre documentation.
> Plus d'informations : <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Liste les interfaces avec des infos détaillées :

`ip address`

- Liste les interfaces sur la couche réseau de façon synthétique :

`ip -brief address`

- Liste les interfaces sur la couche liaison de façon synthétique :

`ip -brief link`

- Affiche la table de routage :

`ip route`

- Affiche les voisins (table ARP) :

`ip neighbour`

- Active/Désactive une interface :

`ip link set {{interface}} up/down`

- Ajoute/Supprime une adresse ip à une interface :

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Ajoute une route par défaut :

`ip route add default via {{ip}} dev {{interface}}`
