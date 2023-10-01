# tcpick

> It is a command-line tool in Linux used for packet sniffing and network traffic analysis.
> It allows you to capture and display TCP connections and their data. You can use it to monitor network traffic on a specific interface or capture traffic to and from a particular host or port.
> More information: <https://linux.die.net/man/8/tcpick>.

- Basic Usage:

`tcpick -i interface -C -h host -p port`

- Advanced Options:

`man tcpick`

- Example to capture traffic on port 80 (HTTP) from a specific host:

`sudo tcpick -i eth0 -C -h 192.168.1.100 -p 80`
