# sshuttle

> Server proxy transparent care tunelează traficul printr-o conexiune SSH.
> Nu necesită root sau orice configurare specială pe serverul SSH la distanță, deși se solicită accesul root pe mașina locală.

- Redirecționați toate traficul IPv4 TCP prin intermediul unui server SSH la distanță:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- De asemenea, redirecționați tot traficul DNS la rezolvatorul DNS implicit al serverului:

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Redirecționați tot traficul, cu excepția celui care este legat pentru o anumită subrețea:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- Utilizați metoda tproxy pentru a transmite toate traficul IPv4 și IPv6:

`sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`
