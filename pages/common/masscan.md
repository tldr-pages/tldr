# Masscan

> Masscan - ultafast network scanner mean to scan the entire Internet as fast as possible
> Best run with elevated priviledges. Nmap compability run masscan --nmap to find out more.
> More information: <https://github.com/robertdavidgraham/masscan>.

- Scan a ip or network subnet for port 443 

`masscan {{ip or CIDR networks or ranges (non-nmap style)}} -p443`

- Scan a class B subnet for the top 100 ports at 100,000 packets per second 

`masscan 10.0.0.0/16 --top-ports 100 --rate 100000`

- Scan a class B subnet, but avoid the ranges in exclude.txt 

`masscan 10.0.0.0/16 ‐‐top-ports 100 ‐‐excludefile exclude.txt`

- Scan the Internet for a port like 443 

`masscan 0.0.0.0/0 -p443 ––rate 10000000`

- Scan the Internet and export to xml output. Other formats include  (-oG Grepable format, -oJ Json format, -oL List format)

`masscan 0.0.0.0/0 -p0-65535 -oX scan.xml`
