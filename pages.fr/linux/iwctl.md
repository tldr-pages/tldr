# iwctl

> Un outil de ligne de commande pour gèrer iwd.
> Plus d'informations : <https://iwd.wiki.kernel.org/gettingstarted>.

- Lancer le mode interactif, dans ce mode vous pouvez entrer les commandes directement, avec de l'autocompletion :

`iwctl`

- Avoir l'aide générale :

`iwctl --help`

- Afficher vos stations wifi :

`iwctl station list`

- Lancer la recherche de réseaux avec une station :

`iwctl station {{station}} scan`

- Afficher les réseaux trouvés par une station :

`iwctl station {{station}} get-networks`

- Se connecter à un réseau avec une station, si des informations de connexion sont nécessaires elles seront démandées :

`iwctl station {{station}} connect {{network_name}}`
