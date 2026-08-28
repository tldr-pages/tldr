# ufw allow

> Autorise le trafic à travers le pare-feu.
> Plus d’informations : <https://manned.org/ufw>.

- Autorise tout trafic sur un port :

`sudo ufw allow {{port}}`

- Autorise le trafic pour un protocole sur un port :

`sudo ufw allow {{port}}/{{protocole}}`

- Autorise le trafic entrant pour un protocole et ajoute un commentaire pour la documentation :

`sudo ufw allow in {{protocole}} comment '{{commentaire}}'`

- Autorise tout trafic depuis une adresse source :

`sudo ufw allow from {{adresse_source}}`

- Autorise tout trafic entrant depuis le sous-réseau 192.168.13.0/24 :

`sudo ufw allow from 192.168.13.0/24`

- Autorise le trafic TCP de 192.168.1.12 vers 192.168.1.100 sur le port 443 :

`sudo ufw allow from 192.168.1.12 to 192.168.1.100 port 443 proto tcp`

- Autorise tout trafic GRE entrant vers 192.168.1.100 sur l’interface eth0 :

`sudo ufw allow in on eth0 to 192.168.1.100 proto gre`
