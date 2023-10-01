# tcpick

> A Linux command-line tool for packet sniffing and network traffic analysis.
> It can capture and display TCP connections and data. It can also monitor network traffic on a specific interface, host, or port.
> More information: <https://linux.die.net/man/8/tcpick>.

- Basic Usage:

`tcpick -i {{interface}} -C -h {{host}} -p {{port}}`

- Advanced Options:

`man tcpick`

- Example to capture traffic on port 80 (HTTP) from a specific host:

`sudo tcpick -i eth0 -C -h 192.168.1.100 -p 80`
