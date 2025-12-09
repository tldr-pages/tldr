# rpcmap.py

> Zoek naar luisterende MSRPC interfaces met behulp van een string binding (bijv. `ncacn_ip_tcp:host[port]`).
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Maak verbinding met een MSRPC interface met behulp van een string binding (bijv. `ncacn_ip_tcp:host[port]`):

`rpcmap.py {{stringbinding}}`

- Bruteforce UUID's zelfs als de MGMT interface beschikbaar is:

`rpcmap.py -brute-uuids {{stringbinding}}`

- Bruteforce bewerkingsnummers (opnums) voor ontdekte UUID's:

`rpcmap.py -brute-opnums {{stringbinding}}`

- Bruteforce hoofdversies van gevonden UUID's:

`rpcmap.py -brute-versions {{stringbinding}}`

- Geef handmatig een doel-IP-adres op:

`rpcmap.py -target-ip {{ip_adres}} {{stringbinding}}`

- Authenticeer naar de RPC interface met gebruikersnaam en wachtwoord:

`rpcmap.py -auth-rpc {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} {{stringbinding}}`

- Authenticeren met NTLM hashes voor RPC:

`rpcmap.py -hashes-rpc {{LMHASH:NTHASH}} {{stringbinding}}`

- Schakel debug-uitvoer in voor uitgebreide informatie:

`rpcmap.py -debug {{stringbinding}}`
