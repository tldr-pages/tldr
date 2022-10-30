# airodump-ng

> Capture packets and display information about wireless networks.
> Part of `aircrack-ng`.
> More information: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Capture packets and display information about a wireless network:

`sudo airodump-ng {{interface}}`

- Capture packets and display information about a wireless network given the MAC address and channel, and save the output to a file:

`sudo airodump-ng --channel {{channel}} --write {{path/to/file}} --bssid {{mac}} {{interface}}`
