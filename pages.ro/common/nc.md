# nc

> Netcat este un utilitar versatil pentru lucrul cu datele TCP sau UDP.
> Mai multe informaţii: <https://nmap.org/ncat>

- Ascultați pe un port specificat și imprimați orice date primite:

`nc -l {{port}}`

- Conectați-vă la un anumit port:

`nc {{ip_address}} {{port}}`

- Stabileşte un timeout:

`nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}`

- Păstrați serverul sus după ce clientul detașează:

`nc -k -l {{port}}`

- Păstrați clientul sus chiar și după EOP:

`nc -q {{timeout}} {{ip_address}}`

- Scanați porturile deschise ale unei gazde specificate:

`nc -v -z {{ip_address}} {{port}}`

- Acționați ca proxy și transmiteți date de la un port local TCP la gazda de la distanță dată:

`nc -l {{local_port}} | nc {{hostname}} {{remote_port}}`
