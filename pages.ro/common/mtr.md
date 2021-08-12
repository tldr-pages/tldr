# mtr

> Traceroute lui Matt: traceroute combinate și instrument de ping.
> Mai multe informaţii: <https://bitwizard.nl/mtr>

- Traceroute la o gazdă și ping continuu toate hamei intermediare:

`mtr {{host}}`

- Dezactivați adresa IP și maparea numelui gazdei:

`mtr -n {{host}}`

- Generează ieșirea după pinging fiecare hop de 10 ori:

`mtr -w {{host}}`

- Forța IP IPv4 sau IPV6:

`mtr -4 {{host}}`

- Așteptați un anumit timp (în secunde) înainte de a trimite un alt pachet la același hamei:

`mtr -i {{seconds}} {{host}}`
