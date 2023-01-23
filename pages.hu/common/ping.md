# ping

> ICMP ECHO_REQUEST csomagok küldése a hálózati hosztoknak. További információ: <https://manned.org/ping>.

- Ping host:

`ping {{host}}`

- Csak meghatározott számú alkalommal pingelhet egy állomáson:

`ping -c {{count}} {{host}}`

- Ping host, megadva a kérések közötti intervallumot másodpercben (alapértelmezett 1 másodperc):

`ping -i {{seconds}} {{host}}`

- Ping host anélkül, hogy szimbolikus neveket próbálna keresni a címekhez:

`ping -n {{host}}`

- Ping host és csengetés, ha csomag érkezik (ha a terminál támogatja):

`ping -a {{host}}`

- Üzenet megjelenítése, ha nem érkezik válasz:

`ping -O {{host}}`
