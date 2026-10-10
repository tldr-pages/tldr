# iptables

> Configureer tabellen, ketens en regels van de Linux kernel IPv4 firewall.
> Gebruik `ip6tables` om regels in te stellen voor IPv6 verkeer.
> Zie ook: `iptables-save`, `iptables-restore`.
> Meer informatie: <https://manned.org/iptables>.

- Bekijk ketens, regels, pakket/byte-tellers en regelnummers voor de filtertabel:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- Stel een ketenbeleidsregel in ([P]):

`sudo iptables {{[-P|--policy]}} {{keten}} {{regel}}`

- Voeg regel toe aan ketenbeleid voor IP:

`sudo iptables {{[-A|--append]}} {{keten}} {{[-s|--source]}} {{ip_adres}} {{[-j|--jump]}} {{regel}}`

- Voeg regel toe aan ketenbeleid voor IP met [p]rotocol en poort in overweging:

`sudo iptables {{[-A|--append]}} {{keten}} {{[-s|--source]}} {{ip_adres}} {{[-p|--protocol]}} {{tcp|udp|icmp|...}} --dport {{poort}} {{[-j|--jump]}} {{regel}}`

- Voeg een NAT-regel toe om al het verkeer van het `192.168.0.0/24` subnet te vertalen naar de publieke IP van de host:

`sudo iptables {{[-t|--table]}} {{nat}} {{[-A|--append]}} {{POSTROUTING}} {{[-s|--source]}} {{192.168.0.0/24}} {{[-j|--jump]}} {{MASQUERADE}}`

- Verwijder ketenregel:

`sudo iptables {{[-D|--delete]}} {{keten}} {{regelnummer}}`
