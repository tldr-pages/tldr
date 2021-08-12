# dig

> Utilitar de căutare DNS.
> Mai multe informaţii: <https://manpages.debian.org/dnsutils/dig.1.html>

- Caută IP-urile asociate cu un nume de gazdă (înregistrări A):

`dig +short {{example.com}}`

- Obțineți un răspuns detaliat pentru un anumit domeniu (înregistrări A):

`dig +noall +answer {{example.com}}`

- Interogare un anumit tip de înregistrare DNS asociat cu un nume de domeniu dat:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Obțineți toate tipurile de înregistrări pentru un nume de domeniu dat:

`dig {{example.com}} ANY`

- Specificați un server DNS alternativ pentru interogare:

`dig @{{8.8.8.8}} {{example.com}}`

- Efectuați o căutare DNS inversă pe o adresă IP (înregistrare PTR):

`dig -x {{8.8.8.8}}`

- Găsiți servere de nume autoritare pentru zonă și afișați înregistrări SOA:

`dig +nssearch {{example.com}}`

- Efectuați interogări iterative și afișați întreaga cale de urmărire pentru a rezolva un nume de domeniu:

`dig +trace {{example.com}}`
