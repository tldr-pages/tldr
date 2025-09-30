# ping6.py

> Simple ICMPv6 ping using Impacket to check if an IPv6 host is reachable.
> Sends ICMPv6 echo requests and listens for echo replies. Requires root privileges for raw socket access (e.g., run with `sudo`).
> More information: <https://github.com/fortra/impacket>.

- Ping an IPv6 host from a specified source IPv6 address:

`ping6.py {{source_ipv6}} {{destination_ipv6}}`

- Ping 2001:db8::2 from 2001:db8::1:

`ping6.py 2001:db8::1 2001:db8::2`
