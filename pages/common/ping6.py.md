# ping6.py

> Check if an IPv6 host is reachable using ICMPv6.
> Sends ICMPv6 echo requests and listens for echo replies.
> Note: Requires root privileges for raw socket access (e.g., run with `sudo`).
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Ping an IPv6 host from a specified source IPv6 address:

`ping6.py {{source_ipv6}} {{destination_ipv6}}`

- Ping 2001:db8::2 from 2001:db8::1:

`ping6.py 2001:db8::1 2001:db8::2`
