# ufw

> Uncomplicated Firewall. Előcsatlakozás az iptables-hez, amelynek célja, hogy megkönnyítse a tűzfal konfigurálását. További információ: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Enable ufw:

`ufw enable`

- Az ufw kikapcsolása:

`ufw disable`

- Az ufw szabályok megjelenítése, a számukkal együtt:

`ufw status numbered`

- Allow incoming traffic on port 5432 on this host with a comment identifying the service:

`ufw allow {{5432}} comment "{{Service}}"`

- Csak a 192.168.0.4-ből a 22-es porton a 192.168.0.4 bármely címére érkező TCP-forgalom engedélyezése ezen az állomáson:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- A 80-as porton érkező forgalom megtagadása ezen az állomáson:

`ufw deny {{80}}`

- Minden UDP-forgalom megtagadása a 8412:8500 tartományba tartozó portokra:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- Egy adott szabály törlése. A szabály száma a `ufw status numbered` parancsból kérhető le:

`ufw delete {{rule_number}}`
