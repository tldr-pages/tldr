# ip address

> Sous-commande de gestion des adresses IP.
> Plus d'informations : <https://manned.org/ip-address>.

- Liste les interfaces réseau et leurs adresses IP associées :

`ip {{[a|address]}}`

- Filtre pour n'afficher que les interfaces réseau actives :

`ip {{[a|address]}} show up`

- Affiche les informations relatives à une interface réseau spécifique :

`ip {{[a|address]}} show dev {{eth0}}`

- Ajoute une adresse IP à une interface réseau :

`ip {{[a|address]}} add {{ip_address}} dev {{eth0}}`

- Supprimer une adresse réseau d'une interface réseau :

`ip {{[a|address]}} delete {{ip_address}} dev {{eth0}}`

- Supprime l'ensemble des adresses IP sur une portée donnée (scope) depuis une interface réseau :

`ip {{[a|address]}} flush dev {{eth0}} scope {{global|host|link}}`
