# ipcalc

> Einfache Operationen und Berechnungen mit IP-Adressen und Netzwerken durchführen.
> Weitere Informationen: <https://manned.org/ipcalc>.

- Zeige Informationen über eine Adresse oder ein Netzwerk mit einer bestimmten Subnetzmaske an:

`ipcalc {{1.2.3.4}} {{255.255.255.0}}`

- Zeige Informationen über eine Adresse oder ein Netzwerk in CIDR-Notation an:

`ipcalc {{1.2.3.4}}/{{24}}`

- Zeige die Broadcast-Adresse einer Adresse oder eines Netzwerks an:

`ipcalc -b {{1.2.3.4}}/{{30}}`

- Zeige die Netzwerkadresse der angegebenen IP-Adresse und Netzmaske an:

`ipcalc -n {{1.2.3.4}}/{{24}}`

- Zeige geografische Informationen zu einer bestimmten IP-Adresse an:

`ipcalc -g {{1.2.3.4}}`
