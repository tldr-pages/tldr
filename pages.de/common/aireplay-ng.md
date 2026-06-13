# aireplay-ng

> Pakete in ein WLAN injizieren.
> Teil von `aircrack-ng`.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Sende eine bestimmten Anzahl an Dissoziation-Paketen mit der MAC-Adresse des Access Points, der MAC-Adresse des Clients und eines Interfaces:

`sudo aireplay-ng --deauth {{anzahl}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
