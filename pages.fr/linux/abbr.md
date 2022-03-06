# abbr

> Gère les abréviations pour le shell Fish.
> Les mots définis par l'utilisateur sont remplacés par des phrases plus longues après leur saisie.
> Plus d'informations : <https://fishshell.com/docs/current/cmds/abbr.html>.

- Ajoute une nouvelle abréviation :

`abbr --add {{nom_abrégé}} {{commande}} {{arguments_de_la_commande}}`

- Renomme une abréviation existante :

`abbr --rename {{ancien_nom}} {{nouveau_nom}}`

- Supprime une abréviation existante :

`abbr --erase {{nom_abrégé}}`

- Importe les abréviations définies sur un autre hôte via SSH :

`ssh {{nom_de_l_hôte}} abbr --show | source`
