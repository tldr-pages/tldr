# nftables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.
> Nftables replaces iptables.

- View current configuration:

`sudo nft list ruleset`

- Add a new table:

`sudo nft add table {{family}} {{table}}`

- Add a new chain:

`sudo nft add chain {{family}} {{table}} {{chain}} \{ type {{type}} hook {{hook}} priority {{priority}} \; \}`

- Add a new rule:

`sudo nft {{[add | insert]}} rule {{family}} {{table}} {{chain}} {{[position]}} {{statement}}`

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- Show rule handles:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- Delete a rule:

`sudo nft delete rule {{family}} {{table}} {{chain}} handle {{handle}}`

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- Save current configuration:

`sudo nft list ruleset > {{/etc/nftables.conf}}`
