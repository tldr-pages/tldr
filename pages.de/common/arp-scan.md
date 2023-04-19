# arp-scan

> ARP Pakete an Host (spezifiert mit IP Adresse oder Hostname) senden um das lokale Netzwerk zu scannen.
> Weitere Informationen: <https://github.com/royhills/arp-scan>.

- Scanne das lokale Netzwerk:

`arp-scan --localnet`

- Ein IP Netzwerk mit einer benutzerdefinierten Bitmaske scannen:

`arp-scan {{netzwerk_adresse}}/{{netzwerk_subnet}}`

- Ein IP Netzwerk innerhalb einer benutzerdefinierten Range scannen:

`arp-scan {{adresse_a}}-{{adresse_b}}`

- Ein IP Netzwerk mit einer benutzerdefinierten Netzmaske scannen:

`arp-scan {{adresse}}:{{netzwerkmaske}}`
