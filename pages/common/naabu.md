# naabu

> A fast port scanner written in Go with a focus on reliability and simplicity.
> Note: Some features are only activated when `naabu` is run with root privileges such as SYN scan.
> More information: <https://docs.projectdiscovery.io/tools/naabu/running>.

- Run a SYN scan against default (top 100) ports of remote host:

`sudo naabu -host {{host}}`

- Display available network interfaces and public IP address of the local host:

`naabu {{[-il|-interface-list]}}`

- Scan all ports of the remote host (CONNECT scan without `sudo`):

`naabu {{[-p|-port]}} - -host {{host}}`

- Scan the top 1000 ports of the remote host:

`naabu {{[-tp|-top-ports]}} 1000 -host {{host}}`

- Scan TCP ports 80, 443 and UDP port 53 of the remote host:

`naabu {{[-p|-port]}} 80,443,u:53 -host {{host}}`

- Show CDN type the remote host is using, if any:

`naabu {{[-p|-port]}} 80,443 -cdn -host {{host}}`

- Run `nmap` from `naabu` for additional functionalities (`nmap` must be installed):

`sudo naabu {{[-v|-verbose]}} -host {{host}} -nmap-cli 'nmap {{-v -T5 -sC}}'`
