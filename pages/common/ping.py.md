# ping.py

> Simple ICMP ping using Impacket to check if an IPv4 host is reachable.
> Sends ICMP echo requests and listens for echo replies. Requires root privileges for raw socket access (e.g., run with `sudo`).
> More information: <https://github.com/fortra/impacket>.

- Ping a host from a specified source IPv4 address:

`ping.py {{source_ipv4}} {{destination_ipv4}}`

- Ping 192.168.1.100 from 192.168.1.10:

`ping.py 192.168.1.10 192.168.1.100`
