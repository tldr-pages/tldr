# ip

> Affiche / manipule l'adressage, le routage, les interfaces et périphériques réseau, les règles de routage et les tunnels.
> Certaines commandes comme `ip {{[a|address]}}ess` ont leur propre documentation.
> Plus d'informations : <https://www.manned.org/ip.8>.

- Liste les interfaces avec des infos détaillées :

`ip {{[a|address]}}`

- Liste les interfaces sur la couche réseau de façon synthétique :

`ip {{[-br a|-brief address]}}`

- Liste les interfaces sur la couche liaison de façon synthétique :

`ip {{[-br l|-brief link]}}`

- Affiche la table de routage :

`ip {{[r|route]}}`

- Affiche les voisins (table ARP) :

`ip {{[n|neighbour]}}`

- Active/Désactive une interface :

`ip {{[l|link]}} set {{interface}} {{up|down}}`

- Ajoute/Supprime une adresse ip à une interface :

`ip {{[a|address]}} add/del {{ip}}/{{mask}} dev {{interface}}`

- Ajoute une route par défaut :

`ip {{[r|route]}} add default via {{ip}} dev {{interface}}`
