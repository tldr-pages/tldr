# aireplay-ng

> Inject packets into a wireless network.
> Part of Aircrack-ng network software suite.
> More information: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Send a specific number of deauthentication packets to a client, given the [a]ccess point's MAC address, the [c]lient's MAC address, and an interface:

`sudo aireplay-ng {{[-0|--deauth]}} {{count}} -a {{ap_mac}} -c {{client_mac}} {{interface}}`
