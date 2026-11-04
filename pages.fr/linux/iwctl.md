# iwctl

> Un outil de ligne de commande pour gérer iwd.
> Voir aussi : `nmcli`, `iw`.
> Plus d'informations : <https://manned.org/iwctl>.

- Lance le mode interactif dans lequel vous pouvez entrer les commandes directement, avec de l'auto-complétion :

`iwctl`

- Affiche vos stations wifi :

`iwctl station list`

- Lance la recherche de réseaux avec une station :

`iwctl station {{station}} scan`

- Affiche les réseaux trouvés par une station :

`iwctl station {{station}} get-networks`

- Se connecte à un réseau avec une station, des informations de connexion seront demandées si nécessaires :

`iwctl station {{station}} connect {{nom_du_réseau}}`

- Affiche l'aide générale :

`iwctl {{[-h|--help]}}`
