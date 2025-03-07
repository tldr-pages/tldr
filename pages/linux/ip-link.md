# ip link

> Manage network interfaces.
> More information: <https://manned.org/ip-link>.

- Show information about all network interfaces:

`ip {{[l|link]}}`

- Show information about a specific network interface:

`ip {{[l|link]}} show {{ethN}}`

- Bring a network interface up or down:

`ip {{[l|link]}} set {{ethN}} {{up|down}}`

- Give a meaningful name to a network interface:

`ip {{[l|link]}} set {{ethN}} alias "{{LAN Interface}}"`

- Change the MAC address of a network interface:

`ip {{[l|link]}} set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- Change the MTU size for a network interface to use jumbo frames:

`ip {{[l|link]}} set {{ethN}} mtu {{9000}}`

- Set the promisc mode status of a device:

`sudo ip {{[l|link]}} set {{ethN}} promisc {{on|off}}`
