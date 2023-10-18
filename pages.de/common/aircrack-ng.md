# aircrack-ng

> WEP und WPA/WPA2 Schlüssel im Kommunikationsaufbau knacken.
> Teil des Aircrack-ng Softwarepakets.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Knacke Schlüssel von abgefangenen Paketen mithilfe von Wortlisten:

`aircrack-ng -w {{pfad/zu/wortliste.txt}} {{pfad/zu/packetdatei.cap}}`

- Knacke Schlüssel von abgefangenen Paketen mithilfe einer Wortliste und der (E)SSID des Access Points:

`aircrack-ng -w {{pfad/zu/wortliste.txt}} -e {{essid}} {{pfad/zu/packetdatei.cap}}`

- Knacke Schlüssel von abgefangenen Paketen mithilfe einer Wortliste und der MAC-Adresse des Access Points:

`aircrack-ng -w {{pfad/zu/wortliste.txt}} --bssid {{mac}} {{pfad/zu/packetdatei.cap}}`
