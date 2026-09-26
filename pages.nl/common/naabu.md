# naabu

> Een snelle poortscanner geschreven in Go, gericht op betrouwbaarheid en eenvoud.
> Opmerking: sommige functies worden alleen geactiveerd wanneer `naabu` wordt uitgevoerd met rootprivileges, zoals SYN-scan.
> Zie ook: `hping3`, `masscan`, `nmap`, `rustscan`, `zmap`.
> Meer informatie: <https://docs.projectdiscovery.io/opensource/naabu/running>.

- Voer een SYN-scan uit tegen de standaard (top 100) poorten van een externe host:

`sudo naabu -host {{host}}`

- Toon beschikbare netwerkinterfaces en het publieke IP-adres van de lokale host:

`naabu {{[-il|-interface-list]}}`

- Scan alle poorten van de externe host (CONNECT-scan zonder `sudo`):

`naabu {{[-p|-port]}} - -host {{host}}`

- Scan de top 1000 poorten van de externe host:

`naabu {{[-tp|-top-ports]}} 1000 -host {{host}}`

- Scan TCP-poorten 80, 443 en UDP-poort 53 van de externe host:

`naabu {{[-p|-port]}} 80,443,u:53 -host {{host}}`

- Toon het CDN-type dat de externe host gebruikt, indien aanwezig:

`naabu {{[-p|-port]}} 80,443 -cdn -host {{host}}`

- Voer `nmap` uit vanuit `naabu` voor extra functionaliteiten (`nmap` moet geïnstalleerd zijn):

`sudo naabu {{[-v|-verbose]}} -host {{host}} -nmap-cli 'nmap {{-v -T5 -sC}}'`
