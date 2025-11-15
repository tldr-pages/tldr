# acme.sh --dns

> Use a DNS-01 challenge to issue a TLS certificate.
> More information: <https://github.com/acmesh-official/acme.sh/wiki>.

- Issue a certificate using an automatic DNS API mode:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- Issue a wildcard certificate (denoted by an asterisk) using an automatic DNS API mode:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Issue a certificate using a DNS alias mode:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- Issue a certificate while disabling automatic Cloudflare/Google DNS polling after the DNS record is added by specifying a custom wait time in seconds:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Issue a certificate using a manual DNS mode:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
