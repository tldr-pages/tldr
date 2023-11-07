# iptables-save

> Sla de `iptables` IPv4 configuratie op.
> Gebruik `ip6tables-save` om hetzelfde te doen voor IPv6.
> Meer informatie: <https://manned.org/iptables-save>.

- Toon de `iptables` configuratie:

`sudo iptables-save`

- Toon de `iptables` configuratie van een specifiek [t]abel:

`sudo iptables-save --table {{tabel}}`

- Sla de `iptables` configuratie op in een bestand:

`sudo iptables-save --file {{pad/naar/bestand}}`
