# networkctl

> Query the status of network links.
> Manage the network configuration using `systemd-networkd`.
> More information: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- List existing links with their status:

`networkctl list`

- Show an overall network status:

`networkctl status`

- Bring network devices up:

`networkctl up {{interface1 interface2 ...}}`

- Bring network devices down:

`networkctl down {{interface1 interface2 ...}}`

- Renew dynamic configurations (e.g. IP addresses received from a DHCP server):

`networkctl renew {{interface1 interface2 ...}}`

- Reload configuration files (.netdev and .network):

`networkctl reload`

- Reconfigure network interfaces (if you edited the config, you need to call `networkctl reload` first):

`networkctl reconfigure {{interface1 interface2 ...}}`
