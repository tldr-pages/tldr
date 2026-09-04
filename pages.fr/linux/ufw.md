# ufw

> Simple pare-feu.
> Interface pour `iptables` visant à simplifier la configuration d’un pare-feu.
> Plus d'informations : <https://manned.org/ufw>.

- Active/désactive `ufw` :

`sudo ufw {{enable|disable}}`

- Affiche les règles `ufw`, avec leurs numéros :

`sudo ufw status numbered`

- Autorise le trafic entrant sur le port 5432 de cet hôte avec un commentaire identifiant le service :

`sudo ufw allow 5432 comment "{{Service}}"`

- Autorise uniquement le trafic TCP de 192.168.0.4 vers n’importe quelle adresse de cet hôte, sur le port 22 :

`sudo ufw allow proto tcp from 192.168.0.4 to any port 22`

- Autorise le trafic provenant de n’importe quelle adresse IP du sous-réseau 192.168.0/24 sur cet hôte, via le port 53, uniquement sur l’interface eth0 :

`sudo ufw allow in on eth0 from 192.168.0.0/24 to any port 53`

- Refuse le trafic sur le port 80 de cet hôte :

`sudo ufw deny 80`

- Refuse tout trafic UDP vers les ports compris entre 8412 et 8500 :

`sudo ufw deny proto udp from any to any port 8412:8500`

- Supprime une règle particulière. Le numéro de la règle peut être récupéré avec la commande `ufw status numbered` :

`sudo ufw delete {{rule_number}}`
