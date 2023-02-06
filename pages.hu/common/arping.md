# arping

> A hálózatban lévő állomáshelyeket az ARP protokoll segítségével fedezi fel és vizsgálja meg. Hasznos a MAC-címek felderítéséhez. További információ: <https://github.com/ThomasHabets/arping>.

- Egy állomás pingelése ARP-kérőcsomagokkal:

`arping {{host_ip}}`

- Egy állomás pingelése egy adott interfészen:

`arping -I {{interface}} {{host_ip}}`

- Egy állomás pingelése és megállítása az első válasznál:

`arping -f {{host_ip}}`

- Egy állomás meghatározott számú pingelése:

`arping -c {{count}} {{host_ip}}`

- ARP-kérőcsomagok továbbítása a szomszédok ARP-tárának frissítéséhez:

`arping -U {{ip_to_broadcast}}`

- A hálózatban lévő duplikált IP-címek felderítése ARP-kérések küldésével, 3 másodperces időkorlátozással:

`arping -D -w {{3}} {{ip_to_check}}`
