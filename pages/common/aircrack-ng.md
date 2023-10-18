# aircrack-ng

> Crack WEP and WPA/WPA2 keys from handshake in captured packets.
> Part of Aircrack-ng network software suite.
> More information: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crack key from capture file using [w]ordlist:

`aircrack-ng -w {{path/to/wordlist.txt}} {{path/to/capture.cap}}`

- Crack key from capture file using [w]ordlist and the access point's [e]ssid:

`aircrack-ng -w {{path/to/wordlist.txt}} -e {{essid}} {{path/to/capture.cap}}`

- Crack key from capture file using [w]ordlist and the access point's MAC address:

`aircrack-ng -w {{path/to/wordlist.txt}} --bssid {{mac}} {{path/to/capture.cap}}`
