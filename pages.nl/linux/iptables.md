# iptables

> Configureer tabellen, ketens en regels van de Linux kernel IPv4 firewall.
> Gebruik `ip6tables` om regels in te stellen voor IPv6 verkeer. Bekijk ook: `iptables-save`, `iptables-restore`.
> Meer informatie: <https://manned.org/iptables>.

- Bekijk ketens, regels, pakket/byte tellers en regelnummers voor de filter tabel:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- Zet keten [P]olicy regel:

`sudo iptables {{[-P|--policy]}} {{keten}} {{regel}}`

- Voeg regel toe aan keten policy voor IP:

`sudo iptables {{[-A|--append]}} {{keten}} {{[-s|--source]}} {{ip}} {{[-j|--jump]}} {{regel}}`

- Voeg regel toe aan keten policy voor IP met [p]rotocol en poort in overweging:

`sudo iptables {{[-A|--append]}} {{keten}} {{[-s|--source]}} {{ip}} {{[-p|--protocol]}} {{tcp|udp|icmp|...}} --dport {{poort}} {{[-j|--jump]}} {{regel}}`

- Voeg een NAT regel toe om al het verkeer van `192.168.0.0/24` subnet te vertalen naar de host's publieke IP:

`sudo iptables {{[-t|--table]}} {{nat}} {{[-A|--append]}} {{POSTROUTING}} {{[-s|--source]}} {{192.168.0.0/24}} {{[-j|--jump]}} {{MASQUERADE}}`

- Verwij[D]er keten regel:

`sudo iptables {{[-D|--delete]}} {{keten}} {{regelnummer}}`
