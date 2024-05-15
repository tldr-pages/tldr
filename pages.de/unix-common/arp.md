# arp

> Den ARP Cache des Systems anzeigen und manipulieren.
> Weitere Informationen: <https://manned.org/arp>.

- Zeige die aktuelle ARP Tabelle an:

`arp -a`

- Leere den gesamten Cache:

`sudo arp -a -d`

- Lösche einen spezifischen Eintrag in der Tabelle:

`arp -d {{addresse}}`

- Erstelle einen Eintrag in der ARP Tabelle:

`arp -s {{adresse}} {{mac_adresse}}`
