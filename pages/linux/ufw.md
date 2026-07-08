# ufw

> Uncomplicated Firewall.
> Frontend for `iptables` aiming to make configuration of a firewall easier.
> More information: <https://manned.org/ufw>.

- Enable/Disable `ufw`:

`sudo ufw {{enable|disable}}`

- Show `ufw` rules, along with their numbers:

`sudo ufw status numbered`

- Allow incoming traffic on port 5432 on this host with a comment identifying the service:

`sudo ufw allow 5432 comment "{{Service}}"`

- Allow only TCP traffic from 192.168.0.4 to any address on this host, on port 22:

`sudo ufw allow proto tcp from 192.168.0.4 to any port 22`

- Allow traffic from any IP on the 192.168.0/24 subnet on this host, through port 53, only on the eth0 interface:

`sudo ufw allow in on {{eth0}} from {{192.168.0.0/24}} to any port {{53}}`

- Deny traffic on port 80 on this host:

`sudo ufw deny 80`

- Deny all UDP traffic to ports in range 8412:8500:

`sudo ufw deny proto udp from any to any port 8412:8500`

- Delete a particular rule. The rule number can be retrieved from the `ufw status numbered` command:

`sudo ufw delete {{rule_number}}`
