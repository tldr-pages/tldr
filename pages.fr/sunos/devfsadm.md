# devfsadm

> Administre `/dev`.
> Maintient l'espace de noms `/dev`.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Recherche de nouveaux disques :

`devfsadm -c disk`

- Nettoie toute pendaison `/dev` liens et recherche un nouvel appareil :

`devfsadm -C -v`

- Marche à sec - sort ce qui serait changé mais ne fait aucune modification :

`devfsadm -C -v -n`
