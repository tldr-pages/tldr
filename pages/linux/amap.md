# amap

> Next-generation scanning tool for pentesters.
> More information: <https://www.thc.org>.

- Scan port 80 on target IP address and print ASCII banner response, omit closed ports, verbosely:

`amap -bqv {{ip_or_hostname}} {{80}}`

- Scan port 1-1024 and capture banners:

`amap -bqv {{ip_or_hostname}} {{1-1024}} -B`

- Scan port 1-1024 and analyze the banners results efficiently:

`amap -bqv {{ip_or_hostname}} {{1-1024}} -A`

- Scan port 1-1024 without banner grabbing and return open ports:

`amap {{ip_or_hostname}} {{1-1024}} -P`
