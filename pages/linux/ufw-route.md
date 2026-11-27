# ufw route

> Manage rules for traffic routed or forwarded through the host.
> IP forwarding must be enabled in the kernel for routed traffic to pass.
> More information: <https://manned.org/ufw>.

- Allow routing traffic from one interface to another:

`sudo ufw route allow in on {{eth0}} out on {{eth1}}`

- Allow routing traffic from a subnet to a destination on a specific port and protocol:

`sudo ufw route allow from {{10.0.0.0/24}} to {{destination_address}} port {{port}} proto {{protocol}}`

- Deny routing traffic to a destination address:

`sudo ufw route deny to {{destination_address}}`

- Reject routed traffic leaving through an interface:

`sudo ufw route reject out on {{interface}}`

- Insert a route rule for a source address at a specific position:

`sudo ufw route insert {{number}} {{allow|deny|reject|limit}} from {{source_address}}`

- Delete a route rule:

`sudo ufw route delete {{rule}}`

- Delete a route rule that denies forwarded traffic to 192.168.0.12:

`sudo ufw route delete deny to 192.168.0.12`
