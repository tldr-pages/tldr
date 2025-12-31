# ip maddress

> Manage multicast addresses.
> More information: <https://manned.org/ip-maddress>.

- List multicast addresses and how many programs are subscribed to them:

`ip {{[m|maddress]}}`

- List device specific addresses:

`ip {{[m|maddress]}} {{[s|show]}} dev {{ethX}}`

- Join a multicast group statically:

`sudo ip {{[m|maddress]}} {{[a|add]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- Leave a static multicast group:

`sudo ip {{[m|maddress]}} {{[d|delete]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- Display help:

`ip {{[m|maddress]}} {{[h|help]}}`
