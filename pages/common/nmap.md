# nmap

> Network exploration tool and security/port scanner.
> Some features only activate when Nmap is run with root privileges.
> More information: <https://nmap.org>.

- Check if an IP address is up, and guess the remote host's operating system:

`nmap -O {{ip_or_hostname}}`

- Try to determine whether the specified hosts are up (ping scan) and what their names and MAC addresses are:

`sudo nmap -sn {{ip_or_hostname}} {{optional_another_address}}`

- Also enable scripts, service detection, OS fingerprinting and traceroute:

`nmap -A {{address_or_addresses}}`

- Scan a specific list of ports (use '-p-' for all ports from 1 to 65535):

`nmap -p {{port1,port2,...,portN}} {{address_or_addresses}}`

- Perform service and version detection of the top 1000 ports using default NSE scripts; writing results ('-oN') to output file:

`nmap -sC -sV -oN {{top-1000-ports.txt}} {{address_or_addresses}}`

- Scan target(s) carefully using 'default and safe' NSE scripts:

`nmap --script "default and safe" {{address_or_addresses}}`

- Scan web server running on standard ports 80 and 443 using all available 'http-*' NSE scripts:

`nmap --script "http-*" {{address_or_addresses}} -p 80,443`

- Perform a stealthy very slow scan ('-T0') trying to avoid detection by IDS/IPS and use decoy ('-D') source IP addresses:

`nmap -T0 -D {{decoy1_ipaddress,decoy2_ipaddress,...,decoyN_ipaddress}} {{address_or_addresses}}`
