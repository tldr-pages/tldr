# ufw insert

> Insert a firewall rule at a specific position in the ruleset.
> The position must be an existing rule number, as shown by `ufw status numbered`.
> More information: <https://manned.org/ufw>.

- Simulate inserting a rule without applying it:

`sudo ufw --dry-run insert {{number}} {{rule}}`

- Insert a rule denying traffic from a source address at the top of the ruleset:

`sudo ufw insert 1 deny from {{source_address}}`

- Insert a rule allowing traffic for a protocol on a port at a specific position:

`sudo ufw insert {{number}} allow {{port}}/{{protocol}}`

- Insert a rule rejecting traffic from a subnet to a port:

`sudo ufw insert {{number}} reject from {{192.168.0.0/24}} to any port {{port}}`

- Insert a rate limiting rule at a specific position:

`sudo ufw insert {{number}} limit {{22}}/{{tcp}}`
