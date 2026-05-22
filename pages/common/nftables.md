# nftables

> Modern Linux kernel packet filtering framework, replacement for iptables.
> More information: <https://wiki.nftables.org>.

- List all current ruleset:

`nft list ruleset`

- Add a table for a specific address family:

`nft add table {{family}} {{table_name}}`

- Add a chain to a table:

`nft add chain {{family}} {{table_name}} {{chain_name}} { type {{filter|nat|route}} hook {{hook}} priority {{priority}} \; }`

- Add a rule to allow incoming TCP traffic on port 80:

`nft add rule {{family}} {{table_name}} {{chain_name}} tcp dport {{80}} accept`

- Flush all rules in a table:

`nft flush table {{family}} {{table_name}}`

- Save the current ruleset to a file:

`nft list ruleset > {{path/to/file.nft}}`

- Load a ruleset from a file:

`nft -f {{path/to/file.nft}}`
