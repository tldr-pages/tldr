# ufw status

> Show the status of Uncomplicated Firewall.
> See also: `ufw`.
> More information: <https://manned.org/ufw>.

- Show whether the firewall is active and list rules:

`sudo ufw status`

- Show rules with numbers (useful before `ufw delete`):

`sudo ufw status numbered`

- Show a verbose status including default policies and listening services:

`sudo ufw status verbose`

- Check status without elevated privileges when permitted:

`ufw status`
