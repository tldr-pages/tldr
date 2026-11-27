# ufw reset

> Reset the firewall to its default state and disable it.
> More information: <https://manned.org/ufw>.

- Simulate resetting the firewall without making changes:

`sudo ufw --dry-run reset`

- Reset the firewall to its default state:

`sudo ufw reset`

- Force reset without asking for confirmation:

`sudo ufw --force reset`
