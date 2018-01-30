# nft

> Allows configuration of tables, chains and rules provided by the Linux kernel firewall.
> Nftables replaces iptables.

- View current configuration:

`sudo nft list ruleset`

- Add a new table with family "inet" and table "filter":

`sudo nft add table {{inet}} {{filter}}`

- Add a new chain to accept all inbound traffic:

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \}`

- Add a new rule to accept several TCP ports:

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- Show rule handles:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- Delete a rule:

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- Save current configuration:

`sudo nft list ruleset > {{/etc/nftables.conf}}`
