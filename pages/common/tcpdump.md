# tcpdump

> Dump traffic on a network.
> More information: <https://www.tcpdump.org>.

- List available network interfaces:

`tcpdump {{[-D|--list-interfaces]}}`

- Capture the traffic of a specific interface:

`sudo tcpdump {{[-i|--interface]}} {{eth0}}`

- Capture all TCP traffic showing contents ([A]SCII) in console:

`sudo tcpdump -A tcp`

- Capture the traffic from or to a host:

`sudo tcpdump host {{www.example.com}}`

- Capture the traffic from a specific interface, source, destination and destination port:

`sudo tcpdump {{[-i|--interface]}} {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- Capture the traffic of a network:

`sudo tcpdump net {{192.168.1.0/24}}`

- Capture all traffic except traffic over port 22 and [w]rite to a dump file:

`sudo tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- [r]ead from a given dump file:

`tcpdump -r {{dumpfile.pcap}}`
