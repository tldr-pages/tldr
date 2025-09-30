# acme.sh --dns

> Usa um desafio DNS-01 para emitir um certificado TLS.
> Mais informações: <https://github.com/acmesh-official/acme.sh/wiki>.

- Emite um certificado usando um modo de DNS API automático:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- Emite um certificado wildcard (denotado por um asterísco (*)) usando um modo DNS API automático:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Emite um certificado usando um modo apelido de DNS:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{apelido-para-exemplo-de-validacao.com}}`

- Emite um certificado enquanto desabilita a pesquisa automática de DNS da Cloudflare/Google depois que o registro DNS for adicionado, especificando um tempo de espera personalizado em segundos:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Emite um certificado usando o modo DNS manual:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
