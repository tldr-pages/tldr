# ipscan

> A fast network scanner designed to be simple to use.
> Also known as Angry IP Scanner.
> More information: <https://www.aldeid.com/wiki/Angry-IPScan#CLI>.

- Scan a specific IP address:

`ipscan {{192.168.0.1}}`

- Scan a range of IP addresses:

`ipscan {{192.168.0.1-254}}`

- Scan a range of IP addresses and save the results to a file:

`ipscan {{192.168.0.1-254}} -o {{path/to/output.txt}}`

- Scan IPs with a specific set of ports:

`ipscan {{192.168.0.1-254}} -p {{80,443,22}}`

- Scan with a delay between requests to avoid network congestion:

`ipscan {{192.168.0.1-254}} -d {{200}}`

- Display help:

`ipscan --help`
