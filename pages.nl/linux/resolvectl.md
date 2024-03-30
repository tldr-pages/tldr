# resolvectl

> Resolve domeinnamen, IPv4 en IPv6 adressen, DNS resource records en services.
> Bekijk en herconfigureer de DNS resolver.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Toon DNS instellingen:

`resolvectl status`

- Resolve de IPv4 en IPv6 adressen voor een of meerdere domeinen:

`resolvectl query {{domein1 domein2 ...}}`

- Verkrijg het domein van een gespecificeerd IP adres:

`resolvectl query {{ip_adres}}`

- Flush alle lokale DNS caches:

`resolvectl flush-caches`

- Toon DNS statistieken (transacties, cache en DNSSEC oordelen):

`resolvectl statistics`

- Verkrijg een MX record van een domein:

`resolvectl --legend={{no}} --type={{MX}} query {{domein}}`

- Resolve een SRV record, bijvoorbeeld _xmpp-server._tcp gmail.com:

`resolvectl service _{{service}}._{{protocol}} {{naam}}`

- Verkrijg een TLS sleutel:

`resolvectl tlsa tcp {{domein}}:443`
