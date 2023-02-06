# ssh-keyscan

> A távoli állomás nyilvános ssh-kulcsainak lekérdezése. További információ: <https://man.openbsd.org/ssh-keyscan>.

- Egy távoli állomás összes nyilvános ssh-kulcsának lekérdezése:

`ssh-keyscan {{host}}`

- Egy adott porton figyelő távoli állomás összes nyilvános ssh-kulcsának lekérdezése:

`ssh-keyscan -p {{port}} {{host}}`

- Egy távoli állomás bizonyos típusú nyilvános ssh-kulcsainak lekérdezése:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- Az ssh known_hosts fájl manuális frissítése egy adott állomás ujjlenyomatával:

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`
