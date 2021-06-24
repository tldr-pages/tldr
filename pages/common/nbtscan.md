# nbtscan

> Scan networks for NetBIOS name information.
> More information: <https://github.com/resurrecting-open-source-projects/nbtscan>.

- Scan a network for NetBIOS names:

`nbtscan {{192.168.0.1/24}}`

- Scan a single IP address:

`nbtscan {{192.168.0.1}}`

- Display verbose output:

`nbtscan -v {{192.168.0.1/24}}`

- Display output in `/etc/hosts` format:

`nbtscan -e {{192.168.0.1/24}}`

- Read IP addresses / networks to scan from a file:

`nbtscan -f {{path/to/file.txt}}`
