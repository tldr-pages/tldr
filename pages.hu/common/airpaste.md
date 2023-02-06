# airpaste

> Üzenetek és fájlok megosztása ugyanazon a hálózaton az mDNS segítségével. További információ: <https://github.com/mafintosh/airpaste>.

- Várjon egy üzenetre, és jelenítse meg azt, ha megkapta:

`airpaste`

- Szöveg küldése:

`echo {{text}} | airpaste`

- Fájl küldése:

`airpaste < {{path/to/file}}`

- Fájl fogadása:

`airpaste > {{path/to/file}}`

- Csatorna létrehozása vagy ahhoz való csatlakozás:

`airpaste {{channel_name}}`
