# ipset

> A tool to create IP sets for firewall rules.
> More information: <https://manned.org/ipset>.

- Create an empty IP set which will contain IP addresses:

`ipset create {{set_name}} hash:ip`

- Destroy a specific IP set:

`ipset destroy {{set_name}}`

- Add an IP address to a specific set:

`ipset add {{set_name}} {{192.168.1.25}}`

- Delete a specific IP address from a set:

`ipset del {{set_name}} {{192.168.1.25}}`

- Save an IP set:

`ipset save {{set_name}} > {{path/to/ip_set}}`
