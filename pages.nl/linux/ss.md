# ss

> Hulpprogramma om sockets te onderzoeken.
> Meer informatie: <https://manned.org/ss>.

- Toon alle TCP/UDP/RAW/UNIX-sockets:

`ss {{[-a|--all]}} {{--tcp|--udp|--raw|--unix}}`

- Filter TCP-sockets op status, alleen/uitgezonderd:

`ss {{state|exclude}} {{bucket|big|connected|synchronized|...}}`

- Toon alle TCP-sockets verbonden met de lokale HTTPS-poort (443):

`ss {{[-t|--tcp]}} src :443`

- Toon alle TCP-sockets die luisteren op de lokale poort 8080:

`ss {{[-lt|--listening --tcp]}} src :8080`

- Toon alle TCP-sockets samen met processen die verbonden zijn met een externe SSH-poort:

`ss {{[-pt|--processes --tcp]}} dst :ssh`

- Toon alle UDP-sockets verbonden op specifieke bron- en bestemmingspoorten:

`ss {{[-u|--udp]}} 'sport == :{{bronpoort}} and dport == :{{bestemmingspoort}}'`

- Toon alle TCP IPv4-sockets lokaal verbonden op het subnet 192.168.0.0/16:

`ss {{[-4t|--ipv4 --tcp]}} src 192.168/16`

- Beëindig een IPv4- of IPv6-socketverbinding met een specifiek bestemmings-IP en poort:

`ss {{[-K|--kill]}} dst {{ip_adres}} dport = {{poort}}`
