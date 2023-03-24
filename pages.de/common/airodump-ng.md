# airodump-ng

> Erfasst Pakete und zeigt Informationen über drahtlose Netzwerke an.
> Teil von `aircrack-ng`.
> Mehr Informationen: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Erfassen von Paketen und Anzeigen von Informationen über ein drahtloses Netzwerk:

`sudo airodump-ng {{interface}}`

- Erfassen von Paketen und Anzeigen von Informationen über ein drahtloses Netzwerk anhand der MAC-Adresse und des Kanals und diese in eine Datei schreiben.  

`sudo airodump-ng --channel {{kanal}} --write {{pfad/zu/datei}} --bssid {{mac}} {{interface}}`
