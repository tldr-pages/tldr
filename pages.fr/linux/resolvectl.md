# resolvectl

> Résout les noms de domaine, les adresses IPV4 et IPv6, les enregistrements de ressources DNS et les services.
> Inspecte et reconfigure le résolveur DNS.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Affiche les paramètres DNS :

`resolvectl status`

- Résout les adresses IPv4 et IPv6 pour un ou plusieurs domaines :

`resolvectl query {{domaine1 domaine2 ...}}`

- Récupère le domaine d'une IP spécifiée :

`resolvectl query {{adresse_ip}}`

- Vide tous les caches DNS locaux :

`resolvectl flush-caches`

- Affiche les statistiques DNS (transactions, cache et verdicts DNSSEC) :

`resolvectl statistics`

- Récupère un enregistrement MX du domaine :

`resolvectl --legend={{no}} --type={{MX}} query {{domaine}}`

- Résout un enregistrement SRV, par exemple _xmpp-server._tcp gmail.com :

`resolvectl service _{{service}}._{{protocole}} {{nom}}`

- Récupère une clé TLS :

`resolvectl tlsa tcp {{domain}}:443`
