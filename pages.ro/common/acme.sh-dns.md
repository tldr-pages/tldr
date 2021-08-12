# acme.sh --dns

> Utilizați o provocare DNS-01 pentru a emite un certificat TLS.
> Mai multe informaţii: <https://github.com/acmesh-official/acme.sh/wiki>

- Eliberați un certificat utilizând un mod API DNS automat:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- Eliberați un certificat wildcard (notat cu un asterisc) utilizând un mod API DNS automat:

`acme.sh --issue --dns {{dns_namesilo}} --domain  {{example.com}} --domain {{*.example.com}}`

- Eliberați un certificat utilizând un mod alias DNS:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- Eliberați un certificat în timp ce dezactivați sondarea automată Cloudflare/Google DNS după ce înregistrarea DNS este adăugată specificând un timp de așteptare personalizat în câteva secunde:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Eliberați un certificat utilizând un mod DNS manual:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
