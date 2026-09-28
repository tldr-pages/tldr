# ip neighbor

> IP-subcommando voor het beheren van neighbor/ARP/NDP-tabellen.
> Meer informatie: <https://manned.org/ip-neighbour>.

- Toon de neighbor/ARP-tabelvermeldingen:

`ip {{[n|neighbor]}}`

- Verwijder vermeldingen in de neighbor-tabel op apparaat `ethX`:

`sudo ip {{[n|neighbor]}} {{[f|flush]}} dev {{ethX}}`

- Voer een neighbor-lookup uit en geef een neighbor-vermelding terug:

`ip {{[n|neighbor]}} {{[g|get]}} {{lookup_ip}} dev {{ethX}}`

- Voeg een ARP-vermelding toe of verwijder deze voor het neighbor IP-adres op `ethX`:

`sudo ip {{[n|neighbor]}} {{add|delete}} {{ip_adres}} lladdr {{mac_adres}} dev {{ethX}} nud reachable`

- Wijzig of vervang een ARP-vermelding voor het neighbor IP-adres op `ethX`:

`sudo ip {{[n|neighbor]}} {{change|replace}} {{ip_adres}} lladdr {{nieuw_mac_adres}} dev {{ethX}}`

- Toon alleen IPv6- of IPv4-neighbors:

`ip {{-6|-4}} {{[n|neighbor]}}`
