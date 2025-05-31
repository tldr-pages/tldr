# ping6.py

> Eenvoudige ICMPv6 ping die Impacket gebruikt om te controleren of een IPv6-host bereikbaar is.
> Stuurt ICMPv6 echo requests en luistert naar echo replies. Vereist root privileges voor raw socket toegang (bijvoorbeeld draaien met `sudo`).
> Meer informatie: <https://github.com/fortra/impacket>.

- Ping een IPv6 host vanaf een opgegeven IPv6 bron-adres:

`ping6.py {{bron_ipv6}} {{bestemmings_ipv6}}`

- Ping 2001:db8::2 vanaf 2001:db8::1:

`ping6.py 2001:db8::1 2001:db8::2`
