# ufw allow

> Allow incoming or outgoing traffic through the Uncomplicated Firewall.
> See also: `ufw`, `ufw deny`.
> More information: <https://manned.org/ufw>.

- Allow incoming traffic on a port:

`sudo ufw allow {{port}}`

- Allow traffic for a specific protocol and port:

`sudo ufw allow {{port}}/{{tcp|udp}}`

- Allow traffic from a specific IP address:

`sudo ufw allow from {{ip_address}}`

- Allow TCP traffic from a specific IP to a port on this host:

`sudo ufw allow proto tcp from {{ip_address}} to any port {{port}}`

- Allow traffic on a specific network interface:

`sudo ufw allow in on {{eth0}} to any port {{port}}`

- Allow traffic using an application profile:

`sudo ufw allow '{{Nginx Full}}'`

- Allow traffic and add a comment describing the rule:

`sudo ufw allow {{port}} comment '{{Description}}'`
