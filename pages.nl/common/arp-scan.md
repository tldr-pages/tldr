# arp-scan

> Verstuur ARP-pakketten naar hosts (gespecificeerd als IP-adressen of hostnames) om het lokale netwerk te scannen.
> Zie ook: `ip neighbor`.
> Meer informatie: <https://github.com/royhills/arp-scan>.

- Scan het huidige lokale netwerk:

`arp-scan {{[-l|--localnet]}}`

- Scan een specifieke host:

`arp-scan {{10.0.0.1}}`

- Scan een IP-netwerk met een aangepast bitmasker:

`arp-scan {{192.168.1.1}}/{{24}}`

- Scan een IP-netwerk binnen een aangepast bereik:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scan een IP-netwerk met een aangepast netmasker:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`

- Specificeer een interface om te gebruiken voor het scannen:

`arp-scan {{10.0.0.1}} {{[-I|--interface]}} {{interface_naam}}`
