# arp

> Show and manipulate your system's ARP cache

- Show current arp table

`arp`

- Delete an entry

`arp -d {{address}}`

- Create an entry

`arp -s {{address}} {{mac address}}`

- Turn arp off or on

`ip link set arp {{off|on}} dev {{interface}}`
