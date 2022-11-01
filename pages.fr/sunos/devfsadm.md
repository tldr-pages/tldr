# devfsadm

> Commande d'administration pour `/dev`. Maintient le `/dev` espace de noms.
> Plus d'information : <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Rechercher de nouveaux disques :

`devfsadm -c disk`

- Nettoyez tout pendaison `/dev` liens et rechercher un nouvel appareil :

`devfsadm -C -v`

- Marche à sec - sortir ce qui serait changé mais ne faire aucune modification :

`devfsadm -C -v -n`
