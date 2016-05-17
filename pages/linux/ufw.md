# ufw

> Uncomplicated Firewall.
> Frontend for iptables aiming to make configuration of a firewall easier.

- Enable ufw:

`ufw enable`

- Disable ufw:

`ufw disable`

- Show ufw rules:

`ufw status`

- Add ufw allow rule:

`ufw allow {{port}} {{service_name}}`

- Example: Allow access to port 1337 from IP 1.2.3.4 using udp:

`ufw allow from 1.2.3.4 to any port 1337 proto udp`

- Add ufw deny rule:

`ufw deny {{port}} {{service_name}}`
