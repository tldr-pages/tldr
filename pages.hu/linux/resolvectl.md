# resolvectl

> Tartománynevek, IPV4 és IPv6 címek, DNS erőforrásrekordok és szolgáltatások feloldása. A DNS-feloldó feltárása és újrakonfigurálása. További információk: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- DNS-beállítások megjelenítése:

`resolvectl status`

- Egy vagy több tartomány IPv4- és IPv6-címének feloldása:

`resolvectl query {{domain1 domain2 ...}}`

- Egy megadott IP tartományának lekérdezése:

`resolvectl query {{ip_address}}`

- A tartomány MX rekordjának lekérdezése:

`resolvectl --legend={{no}} --type={{MX}} query {{domain}}`

- SRV rekord feloldása, például \_xmpp-server.\_tcp gmail.com:

`resolvectl service _{{service}}._{{protocol}} {{name}}`

- Egy e-mail cím nyilvános kulcsának lekérdezése egy OPENPGPKEY DNS-rekordból:

`resolvectl opengpg {{email}}`

- TLS kulcs lekérdezése:

`resolvectl tlsa tcp {{domain}}:443`
