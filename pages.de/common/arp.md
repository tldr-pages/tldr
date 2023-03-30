# arp

> Den ARP Cache des Systems anzeigen und manipulieren
> Weitere Informationen: <https://manned.org/arp>.

- Die aktuelle ARP Tabelle anzeigen lassen:

`arp -a`

- Den gesamten Cache leeren:

`sudo arp -a -d`

- Einen spezifizierten Eintrag in der Tabelle löschen:

`arp -d {{addresse}}`

- Einen Eintrag in der ARP Tabelle erstellen:

`arp -s {{adresse}} {{mac_adresse}}`
