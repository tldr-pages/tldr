# tcpdump

> Dump traffic on a network

- capture the traffic of a specific interface

`tcpdump -i {{eth0}}`

- capture all TCP traffic showing contents (ASCII) in console

`tcpdump -A tcp`

- capture the traffic from or to a host

`tcpdump host {{www.example.com}}`

- capture the traffic from a specific interface, source, destination and port

`tcpdump -i {{eth0}} src {{192.168.1.1}} dest {{192.168.1.2}} and port 80`

- capture the traffic of a network

`tcpdump net {{192.168.1.0/24}}`

- capture all traffic except traffic over port 22 and save to a dump file

`tcpdump -w dumpfile.pcap not port 22`
