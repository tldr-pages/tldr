# ip route show

> Sous commande de gestion de l'affichage des tables de routage.
> Plus d'information : <https://manned.org/ip-route>.

- Affiche la table de routage :

`ip route show`

- Affiche la table de routage principale (identique au premier exemple) :

`ip route show {{main|254}}`

- Affiche la table de routage locale :

`ip route show table {{local|255}}`

- Affiche l'ensemble des tables de routage :

`ip route show table {{all|unspec|0}}`

- Affiche le cache de routage :

`ip route show cache`
