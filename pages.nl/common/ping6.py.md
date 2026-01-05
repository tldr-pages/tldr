# ping6.py

> Controleer of een IPv6-host bereikbaar is door gebruik te maken van ICMPv6.
> Stuurt ICMPv6 echo requests en luistert naar echo replies.
> Opmerking: Vereist root privileges voor raw socket toegang (bijvoorbeeld draaien met `sudo`).
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Ping een IPv6 host vanaf een opgegeven IPv6 bron-adres:

`ping6.py {{bron_ipv6}} {{bestemmings_ipv6}}`

- Ping 2001:db8::2 vanaf 2001:db8::1:

`ping6.py 2001:db8::1 2001:db8::2`
