# ipcalc

> Einfache Operationen und Berechnungen mit IP-Adressen und Netzwerken durchführen.
> Weitere Informationen: <https://manned.org/ipcalc>.

- Zeige Netzwerkinformationen für eine IP-Adresse an:

`ipcalc {{192.168.0.1}}`

- Zeige Netzwerkinformationen unter Verwendung der CIDR-Notation an:

`ipcalc {{192.168.0.1}}/{{24}}`

- Zeige Netzwerkinformationen unter Verwendung einer gepunkteten dezimalen Netzmaske an:

`ipcalc {{192.168.0.1}} {{255.255.255.0}}`

- Unterdrücke Bitweise Ausgabe:

`ipcalc {{[-b|--nobinary]}} {{192.168.0.1}}`

- Teil ein Netzwerk in Blöcke der angegebenen Größe auf:

`ipcalc {{[-s|--split]}} {{size1 size2 size3 ...}} {{192.168.0.1}}`

- Zeige Versionsinformationen an:

`ipcalc {{[-v|--version]}}`
