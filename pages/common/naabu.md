# naabu

> A fast port scanner written in go with a focus on reliability and simplicity. 
> Some features only activate when naabu is run with root privileges such as SYN scan.
> More information: <https://github.com/projectdiscovery/naabu>.

- Run a SYN scan against default (top 100) ports of remote host:

`sudo naabu -host {{host}}`

- Display available network interfaces and public ip of local host:

`naabu -interface-list`

- Scan all ports of remote host (CONNECT scan without sudo):

`naabu -p - -host {{host}}`

- Scan top 1000 ports of remote host:

`naabu -top-ports 1000 -host {{host}}`

- Scan tcp ports 80,443 and udp port 53 of remote host:

`naabu -p 80,443,u:53 -host {{host}}`

- Show CDN type remote host is using, if any:

`naabu -p 80,443 -cdn -host {{host}}`
