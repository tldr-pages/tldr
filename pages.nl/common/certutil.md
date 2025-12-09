# certutil

> Beheer sleutels en certificaten in zowel NSS-databases als andere NSS-tokens.
> Meer informatie: <https://manned.org/certutil>.

- Maak een [N]ieuwe certificaatdatabase aan in de huidige [d]irectory:

`certutil -N -d .`

- Toon alle certificaten in een database:

`certutil -L -d .`

- Toon alle private [S]leutels in een database door het wachtwoord[b]estand te specificeren:

`certutil -K -d . -f {{pad/naar/wachtwoord_bestand.txt}}`

- [V]oeg het ondertekende certificaat toe aan de database van de aanvrager door een [b]ijnaam, [v]ertrouwensattributen en een [i]nvoer-CRT-bestand te specificeren:

`certutil -A -n "{{server_certificaat}}" -t ",," -i {{pad/naar/bestand.crt}} -d .`

- Voeg subject alternative names toe aan een [c]ertificaat met een specifieke sleutelgrootte ([g]):

`certutil -S -f {{pad/naar/wachtwoordbestand.txt}} -d . -t ",," -c "{{server_certificaat}}" -n "{{server_naam}}" -g {{2048}} -s "CN={{common_name}},O={{organisatie}}"`
