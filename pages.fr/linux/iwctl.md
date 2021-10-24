# iwctl

> Un outil de ligne de commande pour gérer iwd.
> Plus d'informations : <https://iwd.wiki.kernel.org/gettingstarted>.

- Lancer le mode interactif, dans ce mode vous pouvez entrer les commandes directement, avec de l'auto-complétion :

`iwctl`

- Avoir l'aide générale :

`iwctl --help`

- Afficher vos stations wifi :

`iwctl station list`

- Lancer la recherche de réseaux avec une station :

`iwctl station {{station}} scan`

- Afficher les réseaux trouvés par une station :

`iwctl station {{station}} get-networks`

- Se connecter à un réseau avec une station, si des informations de connexion sont nécessaires elles seront demandées :

`iwctl station {{station}} connect {{nom_du_réseau}}`
