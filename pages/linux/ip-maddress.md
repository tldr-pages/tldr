# ip maddress

> Manage multicast addresses.
> More information: <https://manned.org/ip-maddress>.

- List multicast addresses and how many programs are subscribed to them:

`ip {{[m|maddress]}}`

- List device specific addresses:

`ip {{[m|maddress]}} show dev {{eth0}}`

- Join a multicast group statically:

`sudo ip {{[m|maddress]}} add {{33:33:00:00:00:02}} dev {{eth0}}`

- Leave a static multicast group:

`sudo ip {{[m|maddress]}} delete {{33:33:00:00:00:02}} dev {{eth0}}`
