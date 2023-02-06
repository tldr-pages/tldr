# cryptcat

> A Cryptcat egy netcat titkosítási képességekkel. További információ: <http://cryptcat.sourceforge.net>.

- \[l\]isten egy megadott \[p\]orton, és kinyomtatja a kapott adatokat:

`cryptcat -k {{password}} -l -p {{port}}`

- Csatlakozás egy adott porthoz:

`cryptcat -k {{password}} {{ip_address}} {{port}}`

- Időkorlát beállítása \[w\]:

`cryptcat -k {{password}} -w {{timeout_in_seconds}} {{ip_address}} {{port}}`

- Ellenőrizze \[z\] egy megadott állomás nyitott portjait:

`cryptcat -v -z {{ip_address}} {{port}}`

- Proxyként viselkedik, és továbbítja az adatokat egy helyi TCP-portról a megadott távoli állomáshoz:

`cryptcat -k {{password}} -l -p {{local_port}} | cryptcat -k {{password}} {{hostname}} {{remote_port}}`
