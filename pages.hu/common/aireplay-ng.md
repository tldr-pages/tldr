# aireplay-ng

> Csomagok bejuttatása egy vezeték nélküli hálózatba. A `aircrack-ng` része. További információ: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Egy hozzáférési pont MAC-címének, egy ügyfél MAC-címének és egy interfésznek a megadásával meghatározott számú disszociációs csomag küldése:

`sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
