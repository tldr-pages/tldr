# airmon-ng

> Aktiver Überwachungsmodus auf Wireless Network Geräten.
> Teil von `aircrack-ng`.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Liste Wireless Geräte und deren Status auf:

`sudo airmon-ng`

- Überwachungsmodus für ein bestimmtes Gerät aktivieren:

`sudo airmon-ng start {{wlan0}}`

- Störende Prozesse killn, die das wireless Gerät verwenden:

`sudo airmon-ng check kill`

- Überwachungsmodus für ein spezifisches Interface deaktivieren:

`sudo airmon-ng stop {{wlan0mon}}`
