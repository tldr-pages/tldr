# ip link

> Manage network interfaces.
> More information: <https://manned.org/ip-link>.

- Show information about all network interfaces:

`ip {{[l|link]}}`

- Show information about a specific network interface:

`ip {{[l|link]}} {{[sh|show]}} {{ethX}}`

- Bring a network interface up or down:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{up|down}}`

- Give a meaningful name to a network interface:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[al|alias]}} "{{LAN Interface}}"`

- Change the MAC address of a network interface:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- Change the MTU size for a network interface to use jumbo frames:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} mtu {{9000}}`

- Set the promisc mode status of a device:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} promisc {{on|off}}`
