# drill

> Efectuați diverse interogări DNS.
> Mai multe informaţii: <https://manned.org/drill>

- Caută IP-urile asociate cu un nume de gazdă (înregistrări A):

`drill {{example.com}}`

- Caută serverul (serverele) de mail asociate cu un anumit nume de domeniu (înregistrare MX):

`drill mx {{example.com}}`

- Obțineți toate tipurile de înregistrări pentru un nume de domeniu dat:

`drill any {{example.com}}`

- Specificați un server DNS alternativ pentru interogare:

`drill {{example.com}} @{{8.8.8.8}}`

- Efectuați o căutare DNS inversă pe o adresă IP (înregistrare PTR):

`drill -x {{8.8.8.8}}`

- Efectuați urme DNSSEC de la serverele rădăcină până la un nume de domeniu:

`drill -TD {{example.com}}`

- Arată înregistrări DNSKEY pentru un nume de domeniu:

`drill -s dnskey {{example.com}}`
