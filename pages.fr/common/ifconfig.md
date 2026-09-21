# ifconfig

> Configurateur des interfaces réseau.
> Plus d'informations : <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Affiche les paramètres réseau d'une interface :

`ifconfig {{nom_interface}}`

- Affiche les détails de toutes les interfaces, y compris les interfaces désactivées :

`ifconfig -a`

- Désactive une interface :

`ifconfig {{nom_interface}} down`

- Active une interface :

`ifconfig {{nom_interface}} up`

- Assigne une adresse IP à une interface :

`ifconfig {{nom_interface}} {{adresse_ip}}`
