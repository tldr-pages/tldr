# arp-scan

> Send ARP packets to hosts on the local network to scan which ones answer.

- Scan the current local network:

`arp-scan --localnet`

- Scan an IP network with a custom bits mask:

`arp-scan {{192.168.1.1}}/{{24}}`

- Scan an IP network within a custom range:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- Scan an IN network with a custom net mask:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
