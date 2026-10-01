# certutil

> Beheer sleutels en certificaten in zowel NSS-databases als andere NSS-tokens.
> Meer informatie: <https://manned.org/certutil>.

- Maak een [N]ieuwe certificaatdatabase aan in de huidige [d]irectory:

`certutil -N -d .`

- Toon alle certificaten in een database:

`certutil -L -d .`

- Toon alle privésleutels in een database door het wachtwoordbestand op te geven:

`certutil -K -d . -f {{pad/naar/wachtwoord_bestand.txt}}`

- Voeg het ondertekende certificaat toe aan de database van de aanvrager, met een bijnaam, vertrouwensattributen en een [i]nvoer-CRT-bestand:

`certutil -A -n "{{server_certificaat}}" -t ",," -i {{pad/naar/bestand.crt}} -d .`

- Voeg subject alternative names toe aan een [c]ertificaat met een specifieke sleutelgrootte ([g]):

`certutil -S -f {{pad/naar/wachtwoordbestand.txt}} -d . -t ",," -c "{{server_certificaat}}" -n "{{server_naam}}" -g {{2048}} -s "CN={{common_name}},O={{organisatie}}"`
