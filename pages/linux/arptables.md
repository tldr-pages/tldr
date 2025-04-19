# arptables

> Manage ARP filtering rules using the nftables backend.
> Part of the `xtables-nft` suite for ARP packet filtering.
> More information: <https://manned.org/arptables>.

- List all ARP rules in the filter table:

`sudo arptables -L`

- Append a rule to drop ARP packets from a specific IP address:

`sudo arptables -A INPUT --source-ip {{192.168.0.1}} -j DROP`

- Delete a specific rule from the INPUT chain by its rule number:

`sudo arptables -D INPUT {{rule_number}}`

- Flush all rules in the filter table:

`sudo arptables -F`

- Set the default policy of the OUTPUT chain to ACCEPT:

`sudo arptables -P OUTPUT ACCEPT`

- Save the current ARP rules to a file:

`sudo arptables-save > {{path/to/file}}`
