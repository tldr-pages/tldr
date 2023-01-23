# nc

> A Netcat egy sokoldalú segédprogram a TCP vagy UDP adatokkal való munkához. További információ: <https://nmap.org/ncat>.

- Figyel egy megadott porton, és kinyomtatja a kapott adatokat:

`nc -l {{port}}`

- Csatlakozás egy adott porthoz:

`nc {{ip_address}} {{port}}`

- Időkorlát beállítása:

`nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}`

- A kiszolgáló fenntartása a kliens leválása után:

`nc -k -l {{port}}`

- A kliens fenntartása az EOF után is:

`nc -q {{timeout}} {{ip_address}}`

- Egy megadott állomás nyitott portjainak vizsgálata:

`nc -v -z {{ip_address}} {{port}}`

- Proxyként viselkedik, és továbbítja az adatokat egy helyi TCP-portról a megadott távoli állomáshoz:

`nc -l {{local_port}} | nc {{hostname}} {{remote_port}}`
