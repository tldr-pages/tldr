# snoop

> Network packet sniffer.
> SunOS equivalent of tcpdump.

- Capture packets on a specific network interface:

`snoop -d {{e1000g0}}`

- Save captured packets in a file instead of displaying them:

`snoop -o {{filename}}`

- Display verbose protocol layer summary of packets from a file:

`snoop -V -i {{filename}}`

- Capture network packets that come from a hostname and go to a given port:

`snoop to port {{port}} from host {{hostname}}`

- Capture and show an hex-dump of network packets exchanged between two IP addresses:

`snoop -x0 -p4 {{ip_address_1}} {{ip_address_2}}`
