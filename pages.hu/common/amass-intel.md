# amass intel

> Nyílt forráskódú információk gyűjtése egy szervezetről, például gyökértartományokról és ASN-ekről. További információ: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Gyökértartományok keresése egy IP-címtartományban:

`amass intel -addr {{192.168.0.1-254}}`

- Használjon aktív felderítési módszereket:

`amass intel -active -addr {{192.168.0.1-254}}`

- Egy tartományhoz kapcsolódó gyökértartományok keresése:

`amass intel -whois -d {{domain_name}}`

- Egy szervezethez tartozó ASN-ek keresése:

`amass intel -org {{organisation_name}}`

- Egy adott autonóm rendszerszámhoz tartozó gyökértartományok keresése:

`amass intel -asn {{asn}}`

- Az eredmények mentése szöveges fájlba:

`amass intel -o {{output_file}} -whois -d {{domain_name}}`
