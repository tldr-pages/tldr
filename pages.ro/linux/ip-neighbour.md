# ip-neighbour

> Subcomanda IP pentru gestionarea tabelelor vecinate/ARP.
> Mai multe informaţii: <https://manned.org/ip-neighbour.8>

- Afișează intrările tabelului vecinate/ARP:

`ip neighbour`

- Eliminați intrările din tabelul vecin de pe dispozitivul `eth0`:

`sudo ip neighbour flush dev {{eth0}}`

- Efectuați o căutare vecină și returnați o intrare vecină:

`ip neighbour get {{lookup_ip}} dev {{eth0}}`

- Adăugați sau ștergeți o intrare ARP pentru adresa IP vecină la `eth0`:

`sudo ip neighbour {{add|del}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- Modificați sau înlocuiți o intrare ARP pentru adresa IP vecină la `eth0`:

`sudo ip neighbour {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`
