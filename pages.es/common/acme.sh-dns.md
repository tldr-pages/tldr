# acme.sh --dns

> Utiliza un desafío DNS-01 para emitir un certificado TLS.
> Más información: <https://github.com/acmesh-official/acme.sh/wiki>.

- Emite un certificado utilizando un modo API DNS automático:

`acme.sh --issue --dns {{gnd_gd}} --domain {{ejemplo.com}}`

- Emite un certificado comodín (marcado con un asterisco) utilizando un modo API DNS automático:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{ejemplo.com}} --domain {{*.ejemplo.com}}`

- Emite un certificado utilizando un modo de alias DNS:

`acme.sh --issue --dns {{dns_cf}} --domain {{ejemplo.com}} --challenge-alias {{alias-para-ejemplo-validacion.com}}`

- Emite un certificado mientras se desactiva el sondeo automático de Cloudflare / Google DNS después de añadir el registro DNS especificando un tiempo de espera personalizado en segundos:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{ejemplo.com}} --dnssleep {{300}}`

- Emite un certificado utilizando un modo DNS manual:

`acme.sh --issue --dns --domain {{ejemplo.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
