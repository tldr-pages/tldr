# hping3

> Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
> Best run with elevated privileges.
> More information: <https://manned.org/hping3>.

- Ping a destination with 4 ICMP ping requests:

`hping3 {{[-1|--icmp]}} {{[-c|--count]}} {{4}} {{ip_or_hostname}}`

- Ping an IP address over UDP on port 80:

`hping3 {{[-2|--udp]}} {{[-p|--destport]}} {{80}} {{[-S|--syn]}} {{ip_or_hostname}}`

- Scan TCP port 80, scanning from the specific local source port 5090:

`hping3 {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} {{80}} {{[-s|--baseport]}} {{5090}} {{ip_or_hostname}}`

- Traceroute using a TCP scan to a specific destination port:

`hping3 {{[-T|--traceroute]}} {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} {{80}} {{ip_or_hostname}}`

- Scan a set of TCP ports on a specific IP address:

`hping3 {{[-8|--scan]}} {{80,3000,9000}} {{[-S|--syn]}} {{ip_or_hostname}}`

- Perform a TCP ACK scan to check if a given host is alive:

`hping3 {{[-c|--count]}} {{2}} {{[-V|--verbose]}} {{[-p|--destport]}} {{80}} {{[-A|--ack]}} {{ip_or_hostname}}`

- Perform a charge test on port 80:

`hping3 --flood {{[-p|--destport]}} {{80}} {{[-S|--syn]}} {{ip_or_hostname}}`
