# ping.py

> Eenvoudige ICMP ping die Impacket gebruikt om te controleren of een IPv4-host bereikbaar is.
> Stuurt ICMP echo requests en luistert naar echo replies. Vereist root privileges voor raw socket toegang (bijvoorbeeld draaien met `sudo`).
> Meer informatie: <https://github.com/fortra/impacket>.

- Ping een host vanaf een opgegeven IPv4 bron-adres:

`ping.py {{bron_ipv4}} {{bestemmings_ipv4}}`

- Ping 192.168.1.100 vanaf 192.168.1.10:

`ping.py 192.168.1.10 192.168.1.100`
