# ip maddress

> Manage multicast addresses.
> More information: <https://manned.org/ip-maddress>.

- List multicast addresses:

`ip maddress`

- List device specific addresses:

`ip maddress show dev {{eth0}}`

- Join a multicast group:

`ip maddr add {{224.0.0.1}} dev {{eth0}}`

- Leave a multicast group:

`ip maddr delete {{224.0.0.1}} dev {{eth0}}`
