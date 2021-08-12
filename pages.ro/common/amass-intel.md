# amass intel

> Colecta Intel open source pe o organizație, cum ar fi domenii rădăcină și ASN-uri.
> Mai multe informaţii: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>

- Găsiți domenii rădăcină într-un interval de adrese IP:

`amass intel -addr {{192.168.0.1-254}}`

- Utilizați metode active de recunoaștere:

`amass intel -active -addr {{192.168.0.1-254}}`

- Găsiți domenii rădăcină legate de un domeniu:

`amass intel -whois -d {{domain_name}}`

- Găsirea ASN aparținând unei organizații:

`amass intel -org {{organisation_name}}`

- Găsiți domenii rădăcină aparținând unui număr de sistem autonom dat:

`amass intel -asn {{asn}}`

- Salvați rezultatele într-un fișier text:

`amass intel -o {{output_file}} -whois -d {{domain_name}}`
