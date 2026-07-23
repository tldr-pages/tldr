# ufw allow

> Allow traffic through the firewall.
> More information: <https://manned.org/ufw>.

- Allow all traffic on a port:

`ufw allow {{port}}`

- Allow traffic for a protocol on a port:

`ufw allow {{port}}/{{protocol}}`

- Allow incoming traffic for a protocol with a comment:

`ufw allow in {{protocol}} comment '{{comment}}'`

- Allow all traffic from a source address:

`ufw allow from {{source_address}}`

- Allow TCP traffic from a source address to a destination address on a port:

`ufw allow proto tcp from {{source_address}} to {{destination_address}} port {{port}}`

- Allow all incoming GRE traffic to a destination address on an interface (e.g., eth0):

`ufw allow in on {{interface}} to {{destination_address}} proto gre`
