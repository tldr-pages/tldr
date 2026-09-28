# pfctl

> Contrôle le dispositif de filtrage de paquets.
> Plus d'informations : <https://man.freebsd.org/cgi/man.cgi?query=pfctl>.

- Active le filtre de paquets :

`sudo pfctl -e`

- Désactive le filtre de paquets :

`sudo pfctl -d`

- Charge les règles depuis un fichier de configuration :

`sudo pfctl -f {{chemin/vers/pf.conf}}`

- Affiche toutes les règles actives :

`pfctl -sr`

- Affiche les informations d’état du filtre de paquets :

`pfctl -s info`

- Supprime toutes les règles :

`sudo pfctl -F rules`
