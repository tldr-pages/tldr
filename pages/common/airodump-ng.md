# airodump-ng

> Capture packets and display information about wireless networks.
> Part of `aircrack-ng`.
> More information: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Capture packets and display information about wireless network(s) on the 2.4GHz band:

`sudo airodump-ng {{interface}}`

- Capture packets and display information about wireless network(s) on the 5GHz band:

`sudo airodump-ng {{interface}} --band a`

- Capture packets and display information about wireless network(s) on both 2.4GHz and 5GHz bands:

`sudo airodump-ng {{interface}} --band abg`

- Capture packets and display information about a wireless network given the MAC address and channel, and save the output to a file:

`sudo airodump-ng --channel {{channel}} --write {{path/to/file}} --bssid {{mac}} {{interface}}`
