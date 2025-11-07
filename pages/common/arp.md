# arp

> Show and manipulate your system's ARP cache.
> More information: <https://manned.org/arp.8>.

- Show the current ARP table:

`arp`

- Show [a]lternative BSD style output format with on fixed columns 

`arp -a`

- [d]elete a specific entry:

`arp -d {{address}}`

- [s]et up a new entry in the ARP table:

`arp -s {{address}} {{mac_address}}`
