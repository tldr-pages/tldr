# nmap

> Hálózati felderítő eszköz és biztonsági / port szkenner. Egyes funkciók csak akkor aktiválódnak, ha az Nmap root jogosultságokkal fut. További információ [: https://nmap.org](https://nmap.org).

- Ellenőrizze, hogy egy IP-cím működik-e, és találja ki a távoli állomás operációs rendszerét:

`nmap -O {{ip_or_hostname}}`

- Megpróbálja megállapítani, hogy a megadott hosztok fent vannak-e (ping vizsgálat), és mi a nevük:

`nmap -sn {{ip_or_hostname}} {{optional_another_address}}`

- Engedélyezze a szkripteket, a szolgáltatásérzékelést, az operációs rendszer ujjlenyomatát és a traceroute-t is:

`nmap -A {{address_or_addresses}}`

- Portok egy adott listájának vizsgálata (a '-p-'-t használja az összes portra 1 és 65535 között):

`nmap -p {{port1,port2,...,portN}} {{address_or_addresses}}`

- A legjobb 1000 port szolgáltatás- és verzióérzékelésének elvégzése az alapértelmezett NSE szkriptek segítségével; az eredmények ('-oN') írása a kimeneti fájlba:

`nmap -sC -sV -oN {{top-1000-ports.txt}} {{address_or_addresses}}`

- A célpont(ok) alapos vizsgálata az 'alapértelmezett és biztonságos' NSE szkriptek használatával:

`nmap --script "default and safe" {{address_or_addresses}}`

- A 80-as és 443-as szabványos portokon futó webkiszolgáló vizsgálata az összes rendelkezésre álló "http-\*" NSE-skript segítségével:

`nmap --script "http-*" {{address_or_addresses}} -p 80,443`

- Lopakodó, nagyon lassú vizsgálat ('-T0'), amely megpróbálja elkerülni az IDS/IPS általi észlelést, és csaló ('-D') forrás IP-címeket használ:

`nmap -T0 -D {{decoy1_ipaddress,decoy2_ipaddress,...,decoyN_ipaddress}} {{address_or_addresses}}`
