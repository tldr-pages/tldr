# cfssl

> Cloudflare's PKI and TLS toolkit.
> See also: `openssl`.
> More information: <https://github.com/cloudflare/cfssl>.

- Show certificate information of a host:

`cfssl certinfo -domain {{www.google.com}}`

- Decode certificate information from a file:

`cfssl certinfo -cert {{path/to/certificate.pem}}`

- Scan host(s) for SSL/TLS issues:

`cfssl scan {{host1 host2 ...}}`

- Display help for a subcommand:

`cfssl {{genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info}} -h`
