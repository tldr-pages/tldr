# arp-scan

> ARP Pakete an Host (spezifiert mit IP Adresse oder Hostname) senden um das lokale Netzwerk zu scannen.
> Weitere Informationen: <https://github.com/royhills/arp-scan>.

- Scanne das lokale Netzwerk:

`arp-scan --localnet`

- Scanne ein IP Netzwerk mit einer benutzerdefinierten Bitmaske:

`arp-scan {{netzwerk_adresse}}/{{netzwerk_subnet}}`

- Scanne ein IP Netzwerk innerhalb einer benutzerdefinierten Range:

`arp-scan {{adresse_a}}-{{adresse_b}}`

- Scanne ein IP Netzwerk mit einer benutzerdefinierten Netzmaske:

`arp-scan {{adresse}}:{{netzwerkmaske}}`
