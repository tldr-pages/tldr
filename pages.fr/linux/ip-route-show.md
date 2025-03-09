# ip route show

> Sous commande de gestion de l'affichage des tables de routage.
> Plus d'informations : <https://manned.org/ip-route>.

- Affiche la table de routage :

`ip {{[r|route]}} show`

- Affiche la table de routage principale (identique au premier exemple) :

`ip {{[r|route]}} show {{main|254}}`

- Affiche la table de routage locale :

`ip {{[r|route]}} show table {{local|255}}`

- Affiche l'ensemble des tables de routage :

`ip {{[r|route]}} show table {{all|unspec|0}}`

- Affiche les routes d'un périphérique donné :

`ip {{[r|route]}} show dev {{eth0}}`

- Affiche les routes d'une portée donnée :

`ip {{[r|route]}} show scope link`

- Affiche le cache de routage :

`ip {{[r|route]}} show cache`

- N'affiche que les routes IPv6 ou IPv4 :

`ip {{-6|-4}} {{[r|route]}} show`
