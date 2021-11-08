# hping3

> Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
> Best run with elevated priviledges.
> More information: <https://github.com/antirez/hping>.

- Ping a destination with 4 ICMP ping requests:

`hping3 --icmp --count {{4}} {{ip_or_hostname}}`

- Scan for port 80 controlling which local source port 5090 initiates the scan:

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}`

- Traceroute to a specific port 80:

`hping3 --traceroute --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}`

- Perform an ACK scan to check if a given host is alive:

`hping3 --count {{2}} --verbose --destport {{80}} -baseport {{5090}} -A {{ip_or_hostname}}`
