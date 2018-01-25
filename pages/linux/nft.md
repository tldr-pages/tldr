# nftables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.
> Nftables replaces iptables.

- View current configuration:

`sudo nft list ruleset`

- List tables:

`sudo nft list tables`

- Add a new table:

`sudo nft add table {{family}} {{table}}`

- Delete a table:

`sudo nft delete table {{family}} {{table}}`

- Add a new chain:

`sudo nft add chain {{family}} {{table}} {{chain}} \{ type {{type}} hook {{hook}} priority {{priority}} \; \}`

- Delete a chain:

`sudo nft delete {{family}} {{table}} {{chain}}`

- Add a new rule:

`sudo nft {{[add | insert]}} rule {{family}} {{table}} {{chain}} {{[position]}} {{statement}}`

- Example rule:

`sudo nft add rule inet filter input tcp dport \{ telnet, ssh, http, https \} accept`

- Show rule handles:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- Delete a rule:

`sudo nft delete rule {{family}} {{table}} {{chain}} handle {{handle}}`

- Save current configuration:

`sudo nft list ruleset > /etc/nftables.conf`

- Clear current configuration:

`sudo nft flush ruleset`
