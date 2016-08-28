# ufw

> Uncomplicated Firewall.
> Frontend for iptables aiming to make configuration of a firewall easier.

- Enable ufw:

`ufw enable`

- Disable ufw:

`ufw disable`

- Show ufw rules, along with their numbers:

`ufw status numbered`

- Allow incoming traffic on port 5432 on this host:

`ufw allow {{5432}}`

- Allow only TCP traffic from 192.168.0.4 to any address on this host, on port 22:

`ufw allow from {{192.168.0.4}} to {{any}} port {{22}} proto {{tcp}}`

- Deny traffic on port 80 on this host:

`ufw deny {{80}}`

- Deny all UDP traffic to port 22:

`ufw deny from {{any}} to {{any}} port {{22}} proto {{udp}}`

- Remove a particular rule. The rule number can be retrieved from the `ufw status numbered` command:

`ufw delete {{rule_number}}`
