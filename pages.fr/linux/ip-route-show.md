# ip route show

> Sous commande de gestion de l'affichage des tables de routage.
> Plus d'informations : <https://manned.org/ip-route>.

- Affiche la table de routage :

`ip route show`

- Affiche la table de routage principale (identique au premier exemple) :

`ip route show {{main|254}}`

- Affiche la table de routage locale :

`ip route show table {{local|255}}`

- Affiche l'ensemble des tables de routage :

`ip route show table {{all|unspec|0}}`

- Affiche les routes d'un périphérique donné :

`ip route show dev {{eth0}}`

- Affiche les routes d'une portée donnée :

`ip route show scope link`

- Affiche le cache de routage :

`ip route show cache`

- N'affiche que les routes IPv6 ou IPv4 :

`ip {{-6|-4}} route show`
