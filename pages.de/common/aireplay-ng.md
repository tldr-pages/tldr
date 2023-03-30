# aireplay-ng

> Pakete in ein WLAN injizieren.
> Teil von `aicraick-ng`.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Senden einer bestimmten Anzahl an deauthentifizierungs Packeten mit der MAC-Adresse des Access POints, der MAC-Adresse des Clients und seines kabellosen interfaces:

`sudo aireplay-ng --deauth {{anzahl}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
