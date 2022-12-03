# aireplay-ng

> Inject packets into a wireless network.
> Part of `aircrack-ng`.
> More information: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Send a specific number of disassociate packets given an access point's MAC address, a client's MAC address and an interface:

`sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
