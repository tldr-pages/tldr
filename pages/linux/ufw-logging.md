# ufw logging

> Configure logging levels for the uncomplicated firewall.
> More information: <https://manned.org/ufw>.

- Turn off firewall logging:

`sudo ufw logging off`

- Set logging to low (logs blocked packets and packets matching log rules):

`sudo ufw logging low`

- Set logging to medium (logs low level plus invalid packets and new connections):

`sudo ufw logging medium`

- Set logging to high (logs medium level plus all packets with rate limiting):

`sudo ufw logging high`

- Set logging to full (logs all packets without rate limiting):

`sudo ufw logging full`
