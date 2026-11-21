# ufw prepend

> Add a firewall rule to the top of the ruleset.
> Unlike `ufw insert`, this does not require an existing rule number.
> More information: <https://manned.org/ufw>.

- Simulate prepending a rule without applying it:

`sudo ufw --dry-run prepend {{rule}}`

- Deny all traffic from a source address before any other rule is evaluated:

`sudo ufw prepend deny from {{source_address}}`

- Deny all traffic from a subnet before any other rule is evaluated:

`sudo ufw prepend deny from {{192.168.0.0/24}}`

- Reject traffic from a source address to a specific port:

`sudo ufw prepend reject from {{source_address}} to any port {{port}}`
