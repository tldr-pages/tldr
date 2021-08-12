# ss

> Utilitate pentru a investiga prize.
> Mai multe informaţii: <https://manned.org/ss.8>

- Arată toate soclurile TCP/UDP/RAW/UNIX:

`ss -a {{-t|-u|-w|-x}}`

- Filtrare prize TCP în funcție de state, numai/exclude:

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- Arată toate soclurile TCP conectate la portul HTTPS local (443):

`ss -t src :{{443}}`

- Arată toate soclurile TCP de ascultare pe portul local 8080:

`ss -lt src :{{8080}}`

- Afișează toate soclurile TCP împreună cu procesele conectate la un port ssh la distanță:

`ss -pt dst :{{ssh}}`

- Afișează toate soclurile UDP conectate la anumite porturi sursă și destinație:

`ss -u 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- Arată toate prizele TCP IPv4 conectate local pe subrețeaua 192.168.0.0/16:

`ss -4t src {{192.168/16}}`
