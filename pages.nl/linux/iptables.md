# iptables

> Configureer tabellen, ketens en regels van de Linux kernel IPv4 firewall.
> Gebruik `ip6tables` om regels in te stellen voor IPv6 verkeer. Zie ook: `iptables-save`, `iptables-restore`.
> Meer informatie: <https://manned.org/iptables>.

- Bekijk ketens, regels, pakket/byte tellers en regelnummers voor de filter tabel:

`sudo iptables --verbose --numeric --list --line-numbers`

- Zet keten [P]olicy regel:

`sudo iptables --policy {{keten}} {{regel}}`

- Voeg regel toe aan keten policy voor IP:

`sudo iptables --append {{keten}} --source {{ip}} --jump {{regel}}`

- Voeg regel toe aan keten policy voor IP met [p]rotocol en poort in overweging:

`sudo iptables --append {{keten}} --source {{ip}} --protocol {{tcp|udp|icmp|...}} --dport {{port}} --jump {{regel}}`

- Voeg een NAT regel toe om al het verkeer van `192.168.0.0/24` subnet te vertalen naar de host's publieke IP:

`sudo iptables --table {{nat}} --append {{POSTROUTING}} --source {{192.168.0.0/24}} --jump {{MASQUERADE}}`

- Verwijder keten regel:

`sudo iptables --delete {{keten}} {{regel_line_number}}`
