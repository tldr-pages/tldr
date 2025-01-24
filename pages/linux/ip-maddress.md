# ip maddress

> Manage multicast addresses.
> More information: <https://manned.org/ip-maddress>.

- List multicast addresses:

`ip maddress`

- List device specific addresses:

`ip maddress show dev {{device_name}}`

- Join a multicast group:

`ip maddr add {{224.0.0.1}} dev {{device_name}}`

- Leave a multicast group:

`ip maddr delete {{224.0.0.1}} dev {{device_name}}`
