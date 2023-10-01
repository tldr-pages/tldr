# tcpick

> A Linux command-line tool for packet sniffing and network traffic analysis.
> It can capture and display TCP connections and data. It can also monitor network traffic on a specific interface, host, or port.
> More information: <https://linux.die.net/man/8/tcpick>.

- Basic usage:

`tcpick -i {{interface}} -C -h {{host}} -p {{port}}`

- Show help:

`tcpick --help`

- Capture traffic on port 80 (HTTP) of a specific host:

`sudo tcpick -i {{eth0}} -C -h {{192.168.1.100}} -p {{80}}`
