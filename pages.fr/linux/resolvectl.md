# resolvectl

> Résout les noms de domaine, les adresses IPV4 et IPv6, les enregistrements de ressources DNS et les services.
> Inspecte et reconfigure le résolveur DNS.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Affiche les paramètres DNS :

`resolvectl status`

- Résout les adresses IPv4 et IPv6 pour un ou plusieurs domaines :

`resolvectl query {{domaine1 domaine2 ...}}`

- Récupère le domaine d'une IP spécifiée :

`resolvectl query {{ip_address}}`

- Récupère un enregistrement MX du domaine :

`resolvectl --legend={{no}} --type={{MX}} query {{domain}}`

- Résout un enregistrement SRV, par exemple _xmpp-server._tcp gmail.com :

`resolvectl service _{{service}}._{{protocol}} {{name}}`

- Récupère la clé publique d'une adresse de courriel à partir d'un enregistrement DNS OPENPGPKEY :

`resolvectl opengpg {{email}}`

- Récupère une clé TLS :

`resolvectl tlsa tcp {{domain}}:443`
