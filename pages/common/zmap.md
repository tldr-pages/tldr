# zmap

> Fast, open-source network scanner for Internet-wide surveys.
> See also: `hping3`, `masscan`, `naabu`, `nmap`, `rustscan`.
> More information: <https://manned.org/zmap>.

- Scan a subnet or full IPv4 space for a specific TCP port (default: 80):

`sudo zmap {{[-p|--target-ports]}} {{port}} {{subnet}}`

- Scan specific ports or port ranges across a subnet:

`sudo zmap {{[-p|--target-ports]}} {{port1,port2-port3,...}} {{subnet}}`

- Output results to a CSV file with custom fields:

`sudo zmap {{[-o|--output-file]}} {{path/to/output_file.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{subnet}}`

- Limit the scan rate to a specific number of packets per second:

`sudo zmap {{[-r|--rate]}} {{packets_per_second}} {{subnet}}`

- Perform a dry run without sending packets:

`zmap {{[-d|--dryrun]}} {{subnet}}`

- Exclude subnets using a blocklist file in CIDR notation:

`sudo zmap {{[-b|--blocklist-file]}} {{path/to/blocklist.txt}} {{subnet}}`

- Set a specific source IP for scan packets:

`sudo zmap {{[-S|--source-ip]}} {{source_ip}} {{subnet}}`

- Cap the number/percentage of targets to probe (e.g. 1000 IP/port pairs):

`sudo zmap {{[-p|--target-ports]}} {{port1,port2-port3}} {{[-n|--max-targets]}} {{1000}} {{subnet}}`
