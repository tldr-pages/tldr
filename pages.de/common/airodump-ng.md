# airodump-ng

> Erfasst Pakete und zeigt Informationen über drahtlose Netzwerke an.
> Teil von `aircrack-ng`.
> Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Erfasse Pakete und zeige Informationen über ein drahtloses Netzwerk an:

`sudo airodump-ng {{interface}}`

- Erfasse Pakete und zeige Informationen über ein drahtloses Netzwerk anhand der MAC-Adresse und des Kanals an, und schreibe diese in eine Datei:

`sudo airodump-ng --channel {{kanal}} --write {{pfad/zu/datei}} --bssid {{mac}} {{interface}}`
