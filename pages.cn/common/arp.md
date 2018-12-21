# arp

> Show and manipulate your system's ARP cache.

- Show current arp table:

`arp -a`

- Clear the entire cache:

`sudo arp -a -d`

- Delete a specific entry:

`arp -d {{address}}`

- Create an entry:

`arp -s {{address}} {{mac_address}}`
