# ifconfig

> Configurateur des interfaces réseau.
> Plus d'informations : <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Affiche les paramètres de réseau d'un adaptateur ethernet :

`ifconfig eth0`

- Affiche les détails de toutes les interfaces, y compris les interfaces désactivées :

`ifconfig -a`

- Désactive l'interface eth0 :

`ifconfig eth0 down`

- Active l'interface eth0 :

`ifconfig eth0 up`

- Assigne une adresse IP à l'interface eth0 :

`ifconfig eth0 {{addresse_ip}}`
