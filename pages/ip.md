# ip

> Networking utilities collection.

- Check address of all interfaces:

`ip {{addr}}`

- Add IPv4 address for eth1:

`ip {{addr}} add 1.2.3.4/24 dev eth1`

- Bring eth1 up:

`ip {{link}} set eth1 up`

- Add subnet route for eth1:

`ip {{route}} add 1.2.3.0/24 dev eth1`

- Given destination IP show which route wll be used:

`ip {{route}} get 8.8.8.8`

- Using shortcut:

`ip {{a}}`
