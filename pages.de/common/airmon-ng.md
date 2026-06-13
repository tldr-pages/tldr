# airmon-ng

> Aktiveren des Überwachungsmodus auf Wireless Network Geräten.
> Teil von `aircrack-ng`.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Liste Wireless Geräte und deren Status auf:

`sudo airmon-ng`

- Aktiviere den Überwachungsmodus für ein bestimmtes Gerät:

`sudo airmon-ng start {{wlan0}}`

- Kille störende Prozesse, die das Wireless Gerät verwenden:

`sudo airmon-ng check kill`

- Deaktiviere den Überwachungsmodus für ein spezifisches Interface:

`sudo airmon-ng stop {{wlan0mon}}`
