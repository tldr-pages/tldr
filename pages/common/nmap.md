# nmap

> Used to discover resources in a network by scanning.
> Efficient when using with root privileges.
> More Information: <https://nmap.org>.

- Scan against an IP address:

`nmap {{ip_address}}`

- Detecting the hosts in a network:

`nmap -sn {{ip_range}}`

- Port Scanning:

`nmap -p {{port_number}} {{ip_address}}` 

- Service Scanning (Require root privileges):

`nmap -sV {{ip_address}}`

- OS Scanning (Require root privileges):

`nmap -O {{ip_address}}`

- TCP or UDP scanning (Require root privileges):

`nmap {{-sT|-sU}} {{ip_address}}`

- Script Scanning (located at /usr/share/nmap/scripts):

`nmap --script {{script_name}} {{ip_address}}`
