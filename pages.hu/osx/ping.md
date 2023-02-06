# ping

> ICMP ECHO_REQUEST csomagok küldése a hálózati hosztoknak. További információ: <https://ss64.com/osx/ping.html>.

- A megadott állomás pingelése:

`ping "{{hostname}}"`

- Egy állomás meghatározott számú pingelése:

`ping -c {{count}} "{{host}}"`

- Ping `host`, megadva a kérések közötti intervallumot `seconds` -ben (alapértelmezett 1 másodperc):

`ping -i {{seconds}} "{{host}}"`

- A `host` pingelése anélkül, hogy megpróbálná megkeresni a címek szimbolikus neveit:

`ping -n "{{host}}"`

- Ping `host` és csengetés, amikor csomag érkezik (ha a terminál támogatja):

`ping -a "{{host}}"`

- Ping `host` és kiírja a csomag fogadásának időpontját (ez az opció egy Apple-kiegészítés):

`ping --apple-time "{{host}}"`
