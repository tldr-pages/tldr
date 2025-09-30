# zmap

> Fast, open-source network scanner for Internet-wide surveys.
> More information: <https://manned.org/zmap>.

- Scan a subnet or full IPv4 space for a specific TCP port (default: 80):

`zmap {{SUBNETS}} {{[-p|--target-ports]}} {{port}}`

- Scan specific ports or port ranges across a subnet:

`zmap {{[-p|--target-ports]}} {{port1,port2-port3,...}} {{SUBNETS}}`

- Output results to a CSV file with custom fields:

`zmap {{[-o|--output-file]}} {{path/to/output_file.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{SUBNETS}}`

- Limit the scan rate to a specific number of packets per second:

`zmap {{[-r|--rate]}} {{packets_per_second}} {{SUBNETS}}`

- Perform a dry run without sending packets:

`zmap {{[-d|--dryrun]}} {{SUBNETS}}`

- Exclude subnets using a blocklist file in CIDR notation:

`zmap {{[-b|--blocklist-file]}} {{path/to/blocklist.txt}} {{SUBNETS}}`

- Set a specific source IP for scan packets:

`zmap {{[-S|--source-ip]}} {{source_ip}} {{SUBNETS}}`

- Cap the number/percentage of targets to probe (e.g. 1000 IP/port pairs):

`zmap {{[-n|--max-targets]}} {{1000}} {{SUBNETS}} {{[-p|--target-ports]}} {{port1,port2-port3}}`
