# snoop

> Network packet sniffer.
> SunOS equivalent of tcpdump.

- Capture packets on network interface e1000g0:

`snoop -d {{e1000g0}}`

- Capture packets to a file:

`snoop -o {{filename}}`

- Display verbose protocol layer summary of packets from a file:

`snoop -V -i {{filename}}`

- Capture network packets that come from hostname and go to port 8000:

`snoop to port 8000 from host {{hostname}}`

- Capture and show network packets in hex and ASCII between two IP addresses:

`snoop -x0 -p4 {{ip address 1}} {{ip address 2}}`
