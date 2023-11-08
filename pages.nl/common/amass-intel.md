# amass intel

> Verzamel open source informatie over een organisatie, zoals hoofddomeinen en ASN's.
> Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Vind hoofddomeinen in een range van IP adressen:

`amass intel -addr {{192.168.0.1-254}}`

- Gebruik actieve verkenningsmethoden:

`amass intel -active -addr {{192.168.0.1-254}}`

- Vind hoofddomeinen gerelateerd aan een domein:

`amass intel -whois -d {{domeinnaam}}`

- Vind ASN's die bij een organisatie horen:

`amass intel -org {{organisatienaam}}`

- Vind hoofddomeinen die bij een bepaald ASN horen:

`amass intel -asn {{asn}}`

- Sla de resultaten op in een tekstbestand:

`amass intel -o {{uitvoer_bestand}} -whois -d {{domeinnaam}}`
