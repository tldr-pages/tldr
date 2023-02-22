# snoop

> Network packet sniffer.
> SunOS equivalent of tcpdump.
> More information: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capture packets on a specific network interface:

`snoop -d {{e1000g0}}`

- Save captured packets in a file instead of displaying them:

`snoop -o {{path/to/file}}`

- Display verbose protocol layer summary of packets from a file:

`snoop -V -i {{path/to/file}}`

- Capture network packets that come from a hostname and go to a given port:

`snoop to port {{port}} from host {{hostname}}`

- Capture and show a hex-dump of network packets exchanged between two IP addresses:

`snoop -x0 -p4 {{ip1}} {{ip2}}`
