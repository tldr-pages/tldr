# ip

> Afișați/manipulați rutarea, dispozitivele, rutarea politicilor și tunelurile.
> Mai multe informaţii: <https://www.man7.org/linux/man-pages/man8/ip.8.html>

- Lista interfețelor cu informații detaliate:

`ip address`

- Lista interfețelor cu informații scurte despre stratul de rețea:

`ip -brief address`

- Lista interfețelor cu informații despre stratul de legătură scurt:

`ip -brief link`

- Afișează tabelul de rutare:

`ip route`

- Arată vecinii (tabelul ARP):

`ip neighbour`

- Faceți o interfață sus/jos:

`ip link set {{interface}} up/down`

- Adăugați/Ștergeți o adresă IP la o interfață:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Adaugă o rută implicită:

`ip route add default via {{ip}} dev {{interface}}`
