# ufw deny

> Deny traffic through the Uncomplicated Firewall.
> See also: `ufw`, `ufw allow`, `ufw status`.
> More information: <https://manned.org/ufw>.

- Deny incoming traffic on a port:

`sudo ufw deny {{port}}`

- Deny traffic for a specific protocol and port:

`sudo ufw deny {{port}}/{{tcp|udp}}`

- Deny traffic from a specific IP address:

`sudo ufw deny from {{ip_address}}`

- Deny UDP traffic to a range of ports:

`sudo ufw deny proto udp from any to any port {{start_port}}:{{end_port}}`

- Deny traffic and add a comment describing the rule:

`sudo ufw deny {{port}} comment "{{Service}}"`
