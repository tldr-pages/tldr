# nmap

> Network exploration tool and security / port scanner

- scan open ports of a single host

`nmap {{192.168.0.1}}`

- discover hosts in the 192.168.0.X area (no port scan)

`nmap -sn {{192.168.0.1/24}}`

- faster scan of a single host (scans for common ports)

`nmap -F {{192.168.0.1}}`

- faster scan of a subnet (scans for common ports)

`nmap -F {{192.168.0.1/24}}`
