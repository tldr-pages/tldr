# arp

> Afișați și manipulați memoria cache ARP a sistemului.
> Mai multe informaţii: <https://manned.org/arp>

- Afișează tabelul ARP curent:

`arp -a`

- Ștergeți întreaga memorie cache:

`sudo arp -a -d`

- Ștergeți o anumită intrare:

`arp -d {{address}}`

- Creați o intrare în tabelul ARP:

`arp -s {{address}} {{mac_address}}`
