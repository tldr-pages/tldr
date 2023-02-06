# ping6

> ICMP ECHO_REQUEST csomagok küldése a hálózati hosztoknak IPv6-címen keresztül. További információ: <https://manned.org/ping6>.

- Pingeljen egy állomáson:

`ping6 {{host}}`

- Egy állomás csak meghatározott számú alkalommal történő pingelése:

`ping6 -c {{count}} {{host}}`

- Pingeljen egy állomáson, megadva a kérések közötti intervallumot másodpercben (alapértelmezett 1 másodperc):

`ping6 -i {{seconds}} {{host}}`

- Egy állomás pingelése anélkül, hogy megpróbálná megkeresni a címek szimbolikus neveit:

`ping6 -n {{host}}`

- Egy állomás pingelése és csengetés, ha csomag érkezik (ha a terminál támogatja):

`ping6 -a {{host}}`
