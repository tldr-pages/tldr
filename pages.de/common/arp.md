# arp

> Den ARP Cache des Systems anzeigen und manipulieren.
> Weitere Informationen: <https://manned.org/arp>.

- Zeige die aktuelle ARP Tabelle an:

`arp -a`

- Den gesamten Cache leeren:

`sudo arp -a -d`

- Einen spezifizierten Eintrag in der Tabelle löschen:

`arp -d {{addresse}}`

- Einen Eintrag in der ARP Tabelle erstellen:

`arp -s {{adresse}} {{mac_adresse}}`
