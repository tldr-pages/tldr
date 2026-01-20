# acme.sh --dns

> Usa una challenge DNS-01 per emettere un certificato TLS.
> Maggiori informazioni: <https://github.com/acmesh-official/acme.sh/wiki>.

- Emetti un certificato usando una modalità DNS API automatica:

`acme.sh --issue --dns {{dns_gd}} --domain {{example.com}}`

- Emetti un certificato wildcard (indicato da un asterisco) usando una modalità DNS API automatica:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Emetti un certificato usando una modalità DNS alias:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-per-la-validazione.example.net}}`

- Emetti un certificato disabilitando il polling automatico dei DNS Cloudflare/Google e specificando un tempo di attesa personalizzato in secondi:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Emetti un certificato usando la modalità DNS manuale:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
