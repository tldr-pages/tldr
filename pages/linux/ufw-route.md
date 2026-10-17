# ufw route

> Configure routing (forwarding) firewall rules.
> More information: <https://manned.org/ufw>.

- Allow routed traffic forwarded from one network interface to another:

`sudo ufw route allow in on {{eth0}} out on {{eth1}}`

- Allow routed traffic to a destination IP and port:

`sudo ufw route allow in on {{eth0}} to {{192.168.1.100}} port {{80}} proto {{tcp}}`

- Deny all routed traffic forwarded from a specific subnet:

`sudo ufw route deny from {{10.0.0.0/8}}`

- Delete a specific route rule:

`sudo ufw route delete allow in on {{eth0}} out on {{eth1}}`

- Delete a route rule by its rule number:

`sudo ufw route delete {{rule_number}}`
