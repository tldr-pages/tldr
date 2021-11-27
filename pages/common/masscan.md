# Masscan

> Network scanner for scanning as fast as possible.
> Best run with elevated priviledges. Nmap compability run `masscan --nmap` to find out more.
> More information: <https://github.com/robertdavidgraham/masscan>.

- Scan an IP or network subnet for port 80:

`masscan {{ip_address|network_prefix}} --ports {{80}}`

- Scan a class B subnet for the top 100 ports at 100,000 packets per second:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- Scan a class B subnet avoiding ranges from a specific exclude file:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{path/to/file}}`

- Scan the Internet for port 443:

`masscan {{0.0.0.0/0}} --ports {{443}} --rate {{10000000}}`

- Scan the Internet for a specific port range and export to a file:

`masscan {{0.0.0.0/0}} --ports {{0-65535}} -output-format {{binary|grepable|json|list|xml}} --output-filename {{path/to/file}}`
