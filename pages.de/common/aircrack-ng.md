# aircrack-ng

> WEP und WPA/WPA2 Schlüssel im Kommunikationsaufbau knacken.
> Teil des Aircrack-ng Softwarepakets.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Schlüssel knacken von abgefangenen Packeten mithilfe von Wortlisten:

`aircrack-ng -w {{pfad/zu/wortliste.txt}} {{pfad/zu/packetdatei.cap}}`

- Schlüssel knacken von abgefangenen Packeten mithilfe einer Wortliste und der (E)SSID des Access Points:

`aircrack-ng -w {{Pfad/zu/Wortliste.txt}} -e {{essid}} {{Pfad/zu/Packetdatei.cap}}`

- Schlüssel knacken von abgefangenen Packeten mithilfe einer Wortliste und der MAC-Adresse des Access Points:

`aircrack-ng -w {{pfad/zu/wortliste.txt}} --bssid {{mac}} {{pfad/zu/packetdatei.cap}}`
