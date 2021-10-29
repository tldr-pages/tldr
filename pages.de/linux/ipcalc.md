# ipcalc

> Einfache Operationen und Berechnungen mit IP-Adressen und Netzwerken durchführen.
> Mehr Informationen: <https://manned.org/ipcalc>.

- Informationen über eine Adresse oder ein Netzwerk mit einer bestimmten Subnetzmaske anzeigen:

`ipcalc {{1.2.3.4}} {{255.255.255.0}}`

- Informationen über eine Adresse oder ein Netzwerk in CIDR-Notation anzeigen:

`ipcalc {{1.2.3.4}}/{{24}}`

- Anzeige der Broadcast-Adresse einer Adresse oder eines Netzwerks:

`ipcalc -b {{1.2.3.4}}/{{30}}`

- Anzeige der Netzwerkadresse der angegebenen IP-Adresse und Netzmaske:

`ipcalc -n {{1.2.3.4}}/{{24}}`

- Anzeige geografischer Informationen zu einer bestimmten IP-Adresse:

`ipcalc -g {{1.2.3.4}}`
