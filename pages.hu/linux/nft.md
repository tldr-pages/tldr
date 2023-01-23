# nft

> Lehetővé teszi a Linux kernel tűzfal által biztosított táblázatok, láncok és szabályok konfigurálását. Az Nftables helyettesíti az iptables-t. További információ: <https://wiki.nftables.org/wiki-nftables/index.php/Main_Page>.

- Az aktuális konfiguráció megtekintése:

`sudo nft list ruleset`

- Új táblázat hozzáadása "inet" családdal és "filter" táblával:

`sudo nft add table {{inet}} {{filter}}`

- Új lánc hozzáadása az összes bejövő forgalom elfogadásához:

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \}`

- Új szabály hozzáadása több TCP-port elfogadásához:

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- NAT-szabály hozzáadása a `192.168.0.0/24` alhálózatból érkező összes forgalom lefordításához az állomás nyilvános IP-címére:

`sudo nft add rule {{nat}} {{postrouting}} ip saddr {{192.168.0.0/24}} {{masquerade}}`

- Szabálykezelők megjelenítése:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- Szabály törlése:

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- Jelenlegi konfiguráció mentése:

`sudo nft list ruleset > {{/etc/nftables.conf}}`
